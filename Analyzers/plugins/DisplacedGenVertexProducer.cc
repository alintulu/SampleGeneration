// system include files
#include <memory>
#include <vector>
#include <unordered_map>
// user include files

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Utilities/interface/Exception.h"


#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJet.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/angle.h"

class DisplacedGenVertexProducer:
    public edm::stream::EDProducer<>
    
{
    private:
        static double distance(const reco::Candidate::Point& p1, const reco::Candidate::Point& p2)
        {
            return std::sqrt((p1-p2).mag2());
        }
        
        static bool ignoreDisplacement(const reco::Candidate& genParticle)
        {
            
            int absPdgId = std::abs(genParticle.pdgId());
            if (absPdgId==111) //ignore pi0 to gamma gamma
            {
                return true;
            }
            
            return false;
        }
        
        static reco::Candidate::Point correctedDisplacement(const reco::Candidate& genParticle)
        {
            //return mother vertex if displacement is ignored
            if (genParticle.mother() and ignoreDisplacement(*genParticle.mother()) and  (distance(genParticle.mother()->vertex(),genParticle.vertex())>1e-10))
            {
                return correctedDisplacement(*genParticle.mother()); //call recursively
            }
            return genParticle.vertex();
        }
        
        static bool displacedDecay(const reco::Candidate& genParticle)
        {
            for (unsigned int idaughter = 0; idaughter<genParticle.numberOfDaughters(); ++idaughter)
            {
                if (distance(genParticle.daughter(idaughter)->vertex(),genParticle.vertex())>1e-10)
                {
                    return true;
                }
            }
            return false;
        }

        edm::InputTag _genParticleInputTag;
        edm::EDGetTokenT<edm::View<reco::GenParticle>> _genParticleToken;
        
        edm::InputTag _genJetInputTag;
        edm::EDGetTokenT<edm::View<reco::GenJet>> _genJetToken;
        
        edm::EDGetTokenT<GenLumiInfoHeader> _genLumiHeaderToken;
        
        std::string lumiCfgStr_;

        virtual void beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& iSetup) override;
        virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup) override;

    public:
        explicit DisplacedGenVertexProducer(const edm::ParameterSet&);
        ~DisplacedGenVertexProducer();

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

};


//
// constructors and destructor

//
DisplacedGenVertexProducer::DisplacedGenVertexProducer(const edm::ParameterSet& iConfig):
    _genParticleInputTag(iConfig.getParameter<edm::InputTag>("srcGenParticles")),
    _genParticleToken(consumes<edm::View<reco::GenParticle>>(_genParticleInputTag)),
    _genJetInputTag(iConfig.getParameter<edm::InputTag>("srcGenJets")),
    _genJetToken(consumes<edm::View<reco::GenJet>>(_genJetInputTag)),
    _genLumiHeaderToken(consumes<GenLumiInfoHeader,edm::InLumi>(edm::InputTag("generator"))),
    lumiCfgStr_("dummy")
    
{
    //produces<std::vector<DisplacedGenVertex>>();
}


DisplacedGenVertexProducer::~DisplacedGenVertexProducer()
{
}

void DisplacedGenVertexProducer::beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& iSetup)
{
		edm::Handle<GenLumiInfoHeader> gen_header;
		iLumi.getByToken(_genLumiHeaderToken, gen_header);
		lumiCfgStr_ = gen_header->configDescription();
		std::cout<<"Lumi transition: "<<lumiCfgStr_<<std::endl;
		// Up to you to decide how to use the string (should probably be a member variable):
		// - Add branch to output ntuple
		// - Make unique ntuple for each signal point
}

// ------------ method called to produce the data  ------------
void
DisplacedGenVertexProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    edm::Handle<edm::View<reco::GenParticle>> genParticleCollection;
    iEvent.getByToken(_genParticleToken, genParticleCollection);
    
    edm::Handle<edm::View<reco::GenJet>> genJetCollection;
    iEvent.getByToken(_genJetToken, genJetCollection);
    
    std::shared_ptr<reco::Candidate::Point> hardInteractionVertex(nullptr);
    
    /*
    std::unordered_map<size_t,unsigned int> genParticleToVertexGroupMap;
    
    
    std::unique_ptr<DisplacedGenVertexCollection> displacedGenVertices(new DisplacedGenVertexCollection());
    edm::RefProd<DisplacedGenVertexCollection> displacedGenVertices_refProd = iEvent.getRefBeforePut<DisplacedGenVertexCollection>();
    */
    for (unsigned int igenParticle = 0; igenParticle < genParticleCollection->size(); ++igenParticle)
    {
        const reco::GenParticle& genParticle = genParticleCollection->at(igenParticle);
        if (genParticle.isHardProcess() and genParticle.numberOfMothers()==2)
        {
            if (!hardInteractionVertex)
            {
                hardInteractionVertex.reset(new reco::Candidate::Point(genParticle.vertex()));
            }
            else if (distance(*hardInteractionVertex,correctedDisplacement(genParticle))>1e-10)
            {
                throw cms::Exception("DisplacedGenVertexProducer: multiple hard interaction vertices found!");
            }
        }
        /*
        //group particles by vertex position
        bool inserted = false;
        for (unsigned int ivertex = 0; ivertex<displacedGenVertices->size(); ++ivertex)
        {
            DisplacedGenVertex& displacedGenVertex = displacedGenVertices->at(ivertex);
            if (distance(displacedGenVertex.vertex,correctedDisplacement(genParticle))<DisplacedGenVertex::MIN_DISPLACEMENT)
            {
                displacedGenVertex.genParticles.push_back(genParticleCollection->ptrAt(igenParticle));
                genParticleToVertexGroupMap[(size_t)&genParticle]=ivertex;
                inserted=true;
                break;
            }
        }
        if (not inserted)
        {
            DisplacedGenVertex displacedGenVertex;
            displacedGenVertex.vertex = genParticle.vertex();
            displacedGenVertex.genParticles.push_back(genParticleCollection->ptrAt(igenParticle));
            displacedGenVertices->push_back(displacedGenVertex);
            genParticleToVertexGroupMap[(size_t)&genParticle]=displacedGenVertices->size()-1;
        }*/
    }
    
    if (not hardInteractionVertex)
    {
        throw cms::Exception("DisplacedVertexProducer: no hard interaction vertex found in event!");
    }  
    
    std::cout<<lumiCfgStr_<<": ";
    /*
    for (unsigned int igenParticle = 0; igenParticle < genParticleCollection->size(); ++igenParticle)
    {
        const reco::GenParticle& genParticle = genParticleCollection->at(igenParticle);
        if (genParticle.pdgId()==1000022)
        {
            std::cout<<std::sqrt((genParticle.vertex()-*hardInteractionVertex).mag2())<<", ";
        }
    }
    */
    for (unsigned int igenParticle = 0; igenParticle < genParticleCollection->size(); ++igenParticle)
    {
        const reco::GenParticle& genParticle = genParticleCollection->at(igenParticle);
        if (genParticle.pdgId()>=4900000)
        {
            std::cout<<"("<<genParticle.pdgId()<<", "<<genParticle.mass()<<"), ";
        }
    }
    
    std::cout<<std::endl;
    
    /*
    for (unsigned int ivertex = 0; ivertex<displacedGenVertices->size(); ++ivertex)
    {
        displacedGenVertices->at(ivertex).hardInteraction = *hardInteractionVertex;
        if (hardInteractionVertex and distance(displacedGenVertices->at(ivertex).vertex,*hardInteractionVertex)<DisplacedGenVertex::MIN_DISPLACEMENT)
        {
            displacedGenVertices->at(ivertex).isHardInteraction=true;
        }
    }
    
    //this helper is required since the reference member cannot be accessed before put
    std::unordered_map<size_t,std::vector<size_t>> daughterVerticesIndices; 
    
    //use longlived particles to link vertex groups
    for (unsigned int igenParticle = 0; igenParticle < genParticleCollection->size(); ++igenParticle)
    {
        const reco::GenParticle& genParticle = genParticleCollection->at(igenParticle);

        if (genParticle.mass()<0)
        {
            continue;
        }
        if (ignoreDisplacement(genParticle) or (not displacedDecay(genParticle)))
        {
            continue;
        }

        unsigned int originVertexGroupIndex = genParticleToVertexGroupMap.at((size_t)&genParticle);
        //book keep summed p4 per vertex group
        std::unordered_map<unsigned int,reco::Candidate::LorentzVector> momentumDistribution;

        for (unsigned int idaughter = 0; idaughter<genParticle.numberOfDaughters(); ++idaughter)
        {
            const reco::Candidate* daughter = genParticle.daughter(idaughter);
            unsigned int daughterVertexGroupIndex = genParticleToVertexGroupMap.at((size_t)daughter);
            if (originVertexGroupIndex!=daughterVertexGroupIndex)
            {
                momentumDistribution[daughterVertexGroupIndex]+=daughter->p4();
            }
        }
        if (genParticle.numberOfDaughters()==0) throw cms::Exception("DisplacedGenVertexProducer: Particle has no daughters in vertex groups");
        //find vertex which shares most of the invariant mass with the long lived particle
        double maxMassRatio = -1;
        int decayVertexIndex = -1;
        for (auto idMomentumPair: momentumDistribution)
        {
            double massRatio = idMomentumPair.second.mass()/std::max<float>(genParticle.mass(),DisplacedGenVertex::MIN_LLP_MASS);
            if (massRatio>maxMassRatio)
            {
                maxMassRatio=massRatio;
                decayVertexIndex = idMomentumPair.first;
            }
        }
        if (decayVertexIndex<0)
        {
            edm::LogError("DisplacedGenVertexProducer")<<"A long lived particle should always connect two vertices";
        }
        else
        {
            //make link
            displacedGenVertices->at(originVertexGroupIndex).sharedMassFraction = maxMassRatio;
            displacedGenVertices->at(originVertexGroupIndex).daughterVertices.push_back(edm::Ref<DisplacedGenVertexCollection>(displacedGenVertices_refProd,decayVertexIndex));
            daughterVerticesIndices[originVertexGroupIndex].push_back(decayVertexIndex);
            edm::Ref<DisplacedGenVertexCollection> motherRef(displacedGenVertices_refProd,originVertexGroupIndex);
            displacedGenVertices->at(decayVertexIndex).motherVertex = std::move(edm::Ptr<DisplacedGenVertex>(motherRef.id(),motherRef.key(),motherRef.productGetter()));
            //store long lived particle in daughter vertex
            displacedGenVertices->at(decayVertexIndex).motherLongLivedParticle = std::move(edm::Ptr<reco::GenParticle>(genParticleCollection,igenParticle));
        }
    }
    
    for (unsigned int ijet = 0; ijet < genJetCollection->size(); ++ijet)
    {
        std::unordered_map<unsigned int,unsigned int> particlesPermatchedVerticesIndex;
        std::unordered_map<unsigned int,reco::Candidate::LorentzVector> p4PermatchedVerticesIndex;
        for (const reco::GenParticle* genParticle: genJetCollection->at(ijet).getGenConstituents())
        {
            auto foundGenParticleIt = genParticleToVertexGroupMap.find((size_t)genParticle); 
            if (foundGenParticleIt!=genParticleToVertexGroupMap.end())
            {
                auto vertexIndexIt = particlesPermatchedVerticesIndex.find(foundGenParticleIt->second);
                
                if (vertexIndexIt==particlesPermatchedVerticesIndex.end())
                {
                    particlesPermatchedVerticesIndex[foundGenParticleIt->second]=1;
                    p4PermatchedVerticesIndex[foundGenParticleIt->second] = genParticle->p4();
                }
                else
                {
                    particlesPermatchedVerticesIndex[foundGenParticleIt->second]+=1;
                    p4PermatchedVerticesIndex[foundGenParticleIt->second]+=genParticle->p4();
                }
            }
        }
        

        if (particlesPermatchedVerticesIndex.size()==0)
        {
            continue;
        }
        else
        {
            float maxShared = 0;
            int maxIndex = -1;

            for (const auto& indexPair: particlesPermatchedVerticesIndex)
            {
                reco::Candidate::Vector vertexVec =  p4PermatchedVerticesIndex[indexPair.first].Vect();
                reco::Candidate::Vector jetVec =  genJetCollection->at(ijet).p4().Vect();
                //calculate projection
                float shared = vertexVec.Dot(jetVec)/jetVec.mag2();
                
                if (shared>maxShared)
                {
                    maxShared = shared;
                    maxIndex = indexPair.first;
                }
  
            }
   
            if (maxIndex>=0)
            {
                displacedGenVertices->at(maxIndex).genJets.push_back(genJetCollection->at(ijet));


                displacedGenVertices->at(maxIndex).jetFractions.push_back(maxShared);
                
            }
        }
    }
    */
    //iEvent.put(std::move(displacedGenVertices));
}



// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DisplacedGenVertexProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}



//define this as a plug-in
DEFINE_FWK_MODULE(DisplacedGenVertexProducer);
