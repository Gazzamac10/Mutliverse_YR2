import streamlit as st
from PIL import Image
from styling import custom_styling

st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

with open( "Styling/styles.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# Create the sidebar links with an indented item
st.sidebar.markdown('''
    <h3>Contents</h3>
    <ul class="custom-sidebar">
        <li><a href="#Home-1">Home</a></li>
        <li><a href="#Overview-1">Overview</a></li>
        <li><a href="#Evaluation-1">Evaluation</a></li>
        <li class="indented-item">&nbsp;&nbsp;&nbsp;<a href="#ISP-1">Information Security Policy</a></li>
        <li class="indented-item">&nbsp;&nbsp;&nbsp;<a href="#Framework-1">Framework</a></li>
        <li class="indented-item">&nbsp;&nbsp;&nbsp;<a href="#R&R">Role's & Responsibilities</a></li>
        <li class="indented-item">&nbsp;&nbsp;&nbsp;<a href="#AC">Access Controls</a></li>
        <li><a href="#Network and security-1">Network and security</a></li>
        <li><a href="#Impact story-1">Impact story</a></li>
    </ul>
''', unsafe_allow_html=True)

st.sidebar.divider()
st.sidebar.markdown('''
    <h3>KSB</h3>
    <h3>Skills</h3>
    <ul>
        <li><a href="#S9-1">S9</a></li>
        <li><a href="#S12-1">S12</a></li>
    </ul>
    <h3>Knowledge</h3>
    <ul>
        <li><a href="#K11-1">K11</a>  <a href="#K11-2">K11</a></li>
        <li><a href="#K16-1">K16</a></li>
        <li><a href="#K57-1">K57</a>  <a href="#K57-2">K57</a></li>
    </ul>
''', unsafe_allow_html=True)

st.markdown('<dummy id="Home-1"></dummy>', unsafe_allow_html=True)
# Add image
image1  = Image.open('Workbased Project\Images\AecomLogo.png')
resized_image1 = image1.resize((400, 100))
st.image(resized_image1)
st.markdown("<h3></h3>", unsafe_allow_html=True)

# Add title
#st.title("Gary McCarthy")
st.write("<h1>Infrastructure and Cybersecurity Report</h1>", unsafe_allow_html=True)

# Add image
image2  = Image.open('Workbased Project\Images\EcoPredict9.png')
resized_image2 = image2.resize((1700, 600))
st.image(resized_image2)
st.markdown("<h3></h3>", unsafe_allow_html=True)

# Add introduction
st.markdown('<dummy id="Overview-1"></dummy>', unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3>Overview:</h3>", unsafe_allow_html=True)
st.markdown("<p>AECOM, a multinational corporation with a global workforce exceeding 80,000 and a presence in major cities worldwide, "
            "appreciates the significance of data as its most valued commodity. In an industry undergoing a digital transformation and "
            "evolving ever more towards automation, the data harvested from such a large and varied portfolio of works is what will "
            "ultimately separate us from our competitors.", unsafe_allow_html=True)

st.markdown("Protecting this valuable asset with robust data security and infrastructure policies is paramount. "
            "The ramifications of a data breach go beyond financial implications, including legal consequences, "
            "productivity loss, and potential damage to the company's reputation.", unsafe_allow_html=True)

st.markdown("This report aims to critically evaluate the current operational frameworks employed across the business "
            "while also looking into how the digital structures team functions within this expansive infrastructure.", unsafe_allow_html=True)

st.markdown("As the Digital Structures Innovation Lead for the UK and Ireland (UKI) region, my scope to impact the security strategy "
            "for the business as a whole is limited, however with Aecom's transition to a cloud based Iaas infrastructure, and direct "
            "access to azure based micro-services, the share responsibility model has come to the forefront and is an area that will "
            "play an evermore important role in our day to day operations.</p>", unsafe_allow_html=True)

st.markdown("With this in mind, I will provide an analysis of the broader business's infrastructure and security landscape "
            "against the specific requirements of the Structures UKI department. A proposal for network and security enhancement within "
            "the Structures department will be presented, accompanied by an exploration of the return on investment from this "
            "proposal.</p>", unsafe_allow_html=True)

st.markdown('<dummy id="Evaluation-1"></dummy><dummy id="K11-1">K11</dummy><dummy id="K16-1">K16</dummy><dummy id="K57-1">K57</dummy>'
            , unsafe_allow_html=True)
st.markdown("<p3>Provide a holistic evaluation report of your organisation's current data"
            " infrastructure. This will encompass a review of data storage solutions, overall"
            " architecture and design, and the balance between cloud and on-premises"
            " storage. Your evaluation should be framed around three main pillars: effciency,"
            " effectiveness, and security. <p3>[K11, K16, K57]</p3></p3>", unsafe_allow_html=True)

st.markdown('<dummy id="Evaluation-1"><dummy id="K11-1">K11</dummy><dummy id="K16-1">K16</dummy><dummy id="K57-1">K57</dummy>'
            , unsafe_allow_html=True)
st.markdown('<dummy id="ISP-1"></dummy>', unsafe_allow_html=True)
st.markdown("<h3>Evaluation of current state:</h3>", unsafe_allow_html=True)
st.markdown("<pb>Information Security Policy:</p>", unsafe_allow_html=True)
st.markdown("<p>AECOM's Information Security Policy, forming the basis for my evaluation, establishes crucial "
            "cybersecurity foundations. Emphasising mandatory requirements and adaptability to business needs, it serves as "
            "a comprehensive guide, prioritising information system protection, ensuring business continuity, and managing "
            "risks within industry standards. The recurring theme of the principle of least privilege reflects AECOM's commitment to "
            "stringent access controls, enhancing overall security. With a broad scope covering all users, systems, and "
            "third-party-managed resources, the policy showcases a holistic commitment to information security in support of business <dummy id='Framework-1'></dummy>"
            "activities.</p>", unsafe_allow_html=True)

st.markdown('<pb>Framework:</pb>', unsafe_allow_html=True)
st.markdown('<p>Aecom has published their information Security policy and is available to all aecom staff through a dedicated cybersecurity internal sharepoint site</p>', unsafe_allow_html=True)
st.markdown('<p>AECOM has implemented a comprehensive information security framework, the Federal Business Services (FBS) Information Security Manual, T2[FBS]-002-PL000, to safeguard its Controlled Unclassified Information (CUI) Environment. This manual establishes policies and standards, aligning with the National Institute of Standards and Technology (NIST) Risk Management Framework (RMF) to ensure a secure network infrastructure. The RMF provides a structured approach to integrating information security and risk management into the system development life cycle.</p>', unsafe_allow_html=True)
st.markdown('<p>Key components of the FBS Information Security Manual include adherence to NIST SP 800-53 controls, which are categorised into families covering aspects like <a href="#AC">access control</a>, awareness and training, audit and accountability, configuration management, contingency planning, and more. AECOM has the flexibility to tailor these controls to meet its unique organisational requirements.</p>', unsafe_allow_html=True)
st.markdown('<p>The manual emphasises the importance of continuous monitoring, information protection, and a robust security architecture. <a href="#R&R">Roles and responsibilities</a> are clearly defined for different stakeholders within AECOM, ensuring accountability and compliance throughout the organisation.</p>', unsafe_allow_html=True)
st.markdown('<p>The NIST Cybersecurity Framework provides a strategic approach to cybersecurity, focusing on five core pillars:</p>', unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
imagenist  = Image.open('NIST5.PNG')
resized_nist = imagenist.resize((1000, 170))
st.image(resized_nist)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown('<p><pi>Identify:</pi> Understand and prioritise assets, risks, and vulnerabilities within the organisation. This pillar involves creating an inventory of resources, data, and users.</p>', unsafe_allow_html=True)
st.markdown('<p><pi>Protect:</pi> Develop and implement safeguards to ensure the confidentiality, integrity, and availability of critical assets. This includes <a href="#AC">access control</a>, encryption, and other protective measures.</p>', unsafe_allow_html=True)
st.markdown('<p><pi>Detect:</pi> Establish mechanisms to identify and detect cybersecurity events promptly. This involves continuous monitoring, anomaly detection, and other tools to recognise potential threats.</p>', unsafe_allow_html=True)
st.markdown('<p><pi>Respond:</pi> Understand and prioritise assets, risks, and vulnerabilities within the organisation. This pillar involves creating an inventory of resources, data, and users.</p>', unsafe_allow_html=True)
st.markdown('<p><pi>Recover:</pi> Develop and implement strategies for efficient and timely recovery from cybersecurity incidents. This involves restoring systems and data to normal operations and learning from incidents to improve future response and recovery efforts.</p>', unsafe_allow_html=True)

st.markdown('<pb>Roles & Responsibilities:</pb><dummy id="R&R"></dummy>', unsafe_allow_html=True)
st.markdown('<p>An effective framework necessitates clear roles and responsibilities for accountability and compliance.</p>', unsafe_allow_html=True)
st.markdown('<p><pi>Executive Leadership:</pi> Holds overall responsibility for policy compliance.</p>', unsafe_allow_html=True)
st.markdown('<p><pi>Chief Information Officer (CIO):</pi> Responsible for allocating resources to maintain and enhance the cybersecurity program.</p>', unsafe_allow_html=True)
st.markdown('<p><pi>Chief Information Security Officer (CISO):</pi> Enforces information security processes and controls, conducts risk assessments, advises on compliance, manages cybersecurity activities, and takes specific actions related to third-party interactions. The detailed breakdown reflects a commitment to a robust cybersecurity program, showcasing a proactive approach.</p>', unsafe_allow_html=True)

st.markdown('<pb>Data Storage & Back-up:</pb>', unsafe_allow_html=True)
st.markdown('<p>AECOM has recently moved to a Cloud Storage hybrid solution that integrates cloud storage with locally hosted infrastructure. The Cloud Storage server functions just like the legacy file server, with several major improvements;</p>', unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Virtually unlimited local file storage (to the AWS Cloud). The cloud storage server works as a local caching server and <ptab3>contains all active data (hot cache) based on employee activity and is automatically saved to the cloud</ptab3></li>", unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Local office storage footprint is downsised to approximately 10% of the current storage capacity without any performance <ptab3>degradation</ptab3>.</li>", unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Eliminates Expensive and inefficient backup of Data, AND Provides Real-Time User Initiated Restore of Data.</li>", unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Promotes Best Practices and Consistency to manage Data across the entire enterprise that enables existing and future <ptab3>collaboration technologies to evolve.</li>", unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Project data is cached and encrypted all the way to the edge, aligns well with our security strategy and renders cyber-attack <ptab3>useless as all data is physically stored centrally.</li>", unsafe_allow_html=True)
st.markdown('<p>Some clients necessitate on-site servers for projects that demand unconnected, on-site storage with no external network access or virtual machines. Aecom retains onsite infrastructure for client lead requests.</p>', unsafe_allow_html=True)

st.markdown("<p>The AECOM IT Operations Team manages backup and recovery operations. The purpose is to minimise data loss in disasters, recover files from the last known good backup, and provide data restoration capabilities for administrative, legal, or operational purposes.</p>", unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Disk-to-Disk (D2D) Backup: Utilising Commvault as the preferred vendor, this involves full server backups stored locally and <ptab3>in the cloud (AWS).</li>", unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Snapshot Backup (Nasuni): Leveraging Nasuni for point-in-time snapshots, providing granular recovery of files, folders, or <ptab3>volumes. Nasuni is a hybrid cloud/network attached solution for file storage and access. Regularly accessed data is cached <ptab3>locally on a Nasuni filer appliance and changes are synced to storage volumes hosted in the cloud. </li>", unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Snapshot Backup (Cloud Native): Using AWS Backup and Azure Backup for short-term or rapid restoration needs.</li>", unsafe_allow_html=True)
st.markdown("<ul class='bullet-point'><li>Microsoft Office 365 Backups: Employing Commvault Metallic as the standard tool for backing up Microsoft 365 data. <ptab3>Commvualt Metallic combines ML-driven automation and AI to deliver risk detection, readiness, and cloud-scale recovery.</li>", unsafe_allow_html=True)

st.markdown('<pb>Access Controls:</pb><dummy id="AC"></dummy>', unsafe_allow_html=True)
st.markdown("<p>Identity Governance and Administration (IGA), also known as identity security, is at the center of Aecom's IT operations, enabling and securing digital identities for all users, applications and data.</p>", unsafe_allow_html=True)
st.markdown("<p>Managing privileged credentials is a difficult challenge for organisations and, when improperly handled, can lead to accounts getting exploited for malicious use such as data exfiltration, data loss, and corruption.</p>", unsafe_allow_html=True)
st.markdown("<p>Ransomware is especially notorious for relying on exploited credentials to spread and propagate within an environment. This puts production data as well as backup data at risk. Aggressive rotation policies provide a better level of security; however, there is greater risk of breaking interoperability within applications that rely on those credentials.</p>", unsafe_allow_html=True)
st.markdown("<p>Privileged Access Management (PAM) is grounded in the principle of least privilege, wherein users only receive the minimum levels of access required to perform their job functions. The principle of least privilege is widely considered to be a cybersecurity best practice and is a fundamental step in protecting privileged access to high-value data and assets</p>", unsafe_allow_html=True)
st.markdown("<p>The AECOM Identification and Authentication Policy (T2[FBS]-002-PL070) outlines measures to uniquely identify and authenticate users in information systems. It distinguishes between local and network access, prohibiting shared accounts unless a risk assessment deems it safe. The policy mandates application-level identification and authentication mechanisms for enhanced security, in addition to system-level procedures. Authentication for various account types involves passwords, PINs, tokens, biometrics, or multifactor authentication (MFA). MFA is specifically required for remote access, especially with privileged accounts and for network access involving sensitive data. The policy encourages the use of replay-resistant authentication mechanisms, including Transport Layer Security (TLS), for network access to privileged accounts.</p>", unsafe_allow_html=True)
st.markdown("<p>In the context of data privacy, privilege isn’t limited to human users alone – especially at a time when machine identities outnumber human identities by 45:1. Non-human entities like servers, applications and automated processes also require identities and privileges.</p>", unsafe_allow_html=True)

col1, col2 = st.columns([0.75,0.25])
with col1:
    st.markdown("<p>Aecom policy dictates the use of approved mechanisms for host or device authentication, such as MAC address filtering (OSI Layer 2), vendor-specific solutions, WPA2 combined with MAC filtering, and IEEE 802.1x. These measures enhance security at different layers of the Open Systems Interconnection (OSI) model.</p>", unsafe_allow_html=True)
    st.markdown("<p>In the context of the OSI model, which conceptualises network communication in seven layers, the mentioned protocols operate at the Data Link Layer (Layer 2) and sometimes extend to the Network Layer (Layer 3). MAC address filtering directly operates at Layer 2, while WPA2 and IEEE 802.1x involve aspects of both Layer 2 and Layer 3. These authentication methods contribute to securing network access, aligning with the layered structure of the OSI model.</p>", unsafe_allow_html=True)
    st.markdown("<p>The policy also recommends implementing network routing controls to restrict specific equipment to connect only from designated external networks or internal subnets. This control enhances security by managing the flow of network traffic based on predefined rules.</p>", unsafe_allow_html=True)
with col2:
    imageOSI  = Image.open('OS_2.png')
    resized_OSI = imageOSI.resize((300, 500))
    st.image(resized_OSI, caption='fig 1')

st.markdown('<pb>System and Communications:</pb>', unsafe_allow_html=True)
st.markdown("<p>AECOM's policy, aligned with NIST 800-53 Rev. 4, sets the foundation for robust System and Communications Protection. The focus on confidentiality, integrity, and availability underscores the commitment to secure operations, ensuring the resilience of systems crucial for both AECOM and its clients.</p>", unsafe_allow_html=True)
st.markdown("<p>AECOM ensures a secure system by separating user functionality from information system management. This involves preventing non-privileged users from accessing management-related functions, segregating internal network zones, and maintaining the isolation of production and non-production environments. Wireless networks are carefully separated to prevent external access, and systems unable to meet security requirements are individually assessed for appropriate controls, potentially exempting them from standard zoning.</p>", unsafe_allow_html=True)

st.markdown('<pb>Microsoft Azure & Cloud Based Services:</pb>', unsafe_allow_html=True)
st.markdown('<p>Direct access to Microsoft Azure places a significant responsibility on the user to adhere to security policies. Azure, as an Infrastructure as a Service (IaaS) provider, operates under a shared responsibility model. In this model, while Azure ensures the security "of" the cloud infrastructure, users are responsible for the security "in" the cloud, including their data, applications, and network configurations.</p>', unsafe_allow_html=True)

st.markdown("<h3>Network and security enhancement proposal(1000 words)</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.475, 0.025, 0.5])
with col1:
    st.markdown("<p>Revit is a 3D modeling software (fig 2) widely used across AECOM and the industry. In the UK&I team alone, we have up to 30 users, and it constitutes a significant portion of our day-to-day operations. As with all our software, repetitive tasks are increasingly automated through coding and access to software APIs. I have been part of a team that built various toolbar add-ins (fig 3) to expedite and automate these tasks.</p>", unsafe_allow_html=True)
    st.markdown("<p>Given the time investment in creating these tools, it has become apparent that monitoring their usage is crucial for measuring return on investment. Several months ago, we deployed a new version of the tool. This time, I was tasked with incorporating code into each button to track usage and return valuable metrics. The data was intended to be stored in a common file on OneDrive, accessible to the BIM management team.</p>", unsafe_allow_html=True)
    st.markdown("<p>However, this approach raised significant issues related to data security, GDPR compliance, and inefficient workflows prone to manual errors and data loss. Moreover, the simultaneous pressing of buttons was causing conflicts during attempts to write to a single file in the OneDrive, leading to the creation of multiple temporary files (fig 4). It is in this context that I propose a new workflow to enhance the network and security measures, establishing a more robust approach to storing and utilising telemetry data.</p>", unsafe_allow_html=True)
with col3:
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    imageOSI  = Image.open('revit.PNG')
    resized_OSI = imageOSI.resize((1200, 800))
    st.image(resized_OSI, caption='fig 2 - Revit modelling software')

    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    imageOSI  = Image.open('Toolbar.PNG')
    resized_OSI = imageOSI.resize((1600, 200))
    st.image(resized_OSI, caption='fig 3 - Aecom in house Toolbar')
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    imageOSI  = Image.open('Pasted image 20231125121933.png')
    resized_OSI = imageOSI.resize((1200, 300))
    st.image(resized_OSI, caption='fig 4 - Current storage system')
    
st.markdown("<h3></h3>", unsafe_allow_html=True)  
imageOSI  = Image.open('pngfind.com-microsoft-png-1121331.png')
resized_OSI = imageOSI.resize((400, 50))
st.image(resized_OSI)
st.markdown("<p>Upon acquiring access to Azure Microservices, my aim was to leverage cloud storage for direct data transmission from the software API. The initial consideration involved evaluating the type and characteristics of the data, along with assessing the frequency of read and write throughput requirements. Given that the telemetry data would be sent sporadically and event driven, Azure Table Storage emerged as the preferred choice over SQL. This decision was influenced by the scalability of Table Storage and its cost-effective pay-as-you-go pricing model.</p>", unsafe_allow_html=True)
st.markdown("<p>With the storage solution determined, the next step was to initiate the data transport process to the table. Adapting the original code responsible for sending data to the current text file, I modified it to enable direct transmission to the Azure Table Storage. It became apparent that embedding storage account credentials within the code posed security risks and vulnerabilities. Additionally, for consistent deployment across all computers utilising the toolbar, a secure and standardised approach was essential. Opting for a serverless solution, I chose an Azure Function App with an HTTP trigger as the most suitable method. To comprehend the data flow through this system and address potential security implications, I recognised the need for a systematic diagram, illustrating the process.</p>", unsafe_allow_html=True)

st.markdown("<h3></h3>", unsafe_allow_html=True)  
imageOSI  = Image.open('Azureserverless1.PNG')
resized_OSI = imageOSI.resize((800, 600))
st.image(resized_OSI)

st.markdown("<p>Using this system data is now sent via the HTTP protocol to an Azure-hosted Function App, which utilises an HTTP trigger to initiate the process. The credentials are verified through Azure Vault, and once authenticated, the Function App processes the data, sending it up to the storage table. All computers send data to the same endpoint, and Azure employs a queue system to process the data sequentially</p>", unsafe_allow_html=True)

st.markdown("<p>Once the data is sent to the storage table, the cloud provider handles cybersecurity. However, it is my responsibility to secure data in transit and address any potential vulnerabilities they may have opened up during the process.</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.475, 0.025, 0.5])
with col1:
    st.markdown("<p><pb>Man-in-the-Middle (MitM) Attacks:</pb> Data transmitted over the internet is susceptible to interception by attackers, who may position themselves between the client and serverless function to eavesdrop or modify data. I switched the protocol to HTTPS to encrypt data in transit and ensure my Function App enforces secure communication to prevent tampering or interception. I also ran a port sniff on the endpoint webpage to check which ports were open</p>", unsafe_allow_html=True)
with col3:
    imageOSI  = Image.open('portsniff100.PNG')
    resized_OSI = imageOSI.resize((600, 400))
    st.image(resized_OSI, caption='fig 5')

