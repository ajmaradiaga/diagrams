# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.sap.integration import *
from diagrams.sap.development import *
from diagrams.sap.database_datamanagement import *
from diagrams.sap.runtimes import *
from diagrams.sap.ai import *

# SAP BTP Solution Diagrams and Icons guidelines colours
L0_BLUE_COLOUR = "#0070F2"
L0_FILLED_COLOUR = "#EBF8FF"
L1_BLUE_COLOUR = "#0040B0"
L1_FILLED_COLOUR = "#EBF8FF"
L1_BLUE_COLOUR = "#002A86"
SUCCESS_GREEN_COLOUR = "#188918"
SUCCESS_FILLED_COLOUR = "#F5FAE5"

FIX_GREY_COLOUR = "#7F7F7F"
NON_SAP_AREA_COLOUR = "#595959"

with Diagram("Creating architecture diagrams with code", show=False):
    with Cluster("SAP Business Technology Platform", graph_attr= {"bgcolor": L0_FILLED_COLOUR, "pencolor": L0_BLUE_COLOUR}) as btp_cluster:

        with Cluster(label="Development", graph_attr= {"bgcolor": "white", "pencolor": L0_BLUE_COLOUR}) as development_cluster:
            CloudFoundryRuntime_Circled("Cloud Foundry") - Edge(color="transparent") - \
            KymaRuntime("Kyma") - Edge(color="transparent") - \
            Html5ApplicationRepositoryService_Circled("HTML5\nApplications") - Edge(color="transparent") - \
            SAPHANACloud_Circled("HANA Cloud")  - Edge(color="transparent") - \
            Postgresql("PostgreSQL") - Edge(color="transparent") - \
            Redis("Redis")
        
        with Cluster("Integration", graph_attr= {"bgcolor": "white", "pencolor": L1_BLUE_COLOUR}) as integration_cluster:
            integration_cluster.dot.graph_attr["bgcolor"] = "white"
            IntegrationSuite_Circled("Cloud Integration") - Edge(color="transparent") - APIManagement_Circle("API Management") - Edge(color="transparent") - EventMesh_Circled("Event Mesh")  - Edge(color="transparent") - \
            OpenConnectors_Circle("Open Connectors") - Edge(color="transparent") - CloudConnector_Circle("Cloud Connector")  - Edge(color="transparent") - IntegrationAdvisor_Circle("Integration Advisor")
        
        with Cluster("Artificial Intelligence", graph_attr= {"bgcolor": SUCCESS_FILLED_COLOUR, "pencolor": SUCCESS_GREEN_COLOUR}) as ai_cluster:
            DocumentClassification_Circled("Document\nClassification") - Edge(color="transparent") - \
            DocumentInformationExtraction_Circled("Document Information\nExtraction") - Edge(color="transparent") - \
            ServiceTicketIntelligence_Circled("Service Ticket\nIntelligence")
            
