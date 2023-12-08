import streamlit as st
from PIL import Image
from styling import custom_styling

st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

with open( "styling/styles.css" ) as css:
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

st.markdown('<dummy id="Home-1"></dummy>', unsafe_allow_html=True)
# Add image
image1  = Image.open('AecomLogo.png')
resized_image1 = image1.resize((400, 100))
st.image(resized_image1)
st.markdown("<h3></h3>", unsafe_allow_html=True)


# Add title
#st.title("Gary McCarthy")
st.write("<h1>Infrastructure and Cybersecurity Report</h1>", unsafe_allow_html=True)

# Add image
image2  = Image.open('RequestFail.png')
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

st.markdown('<dummy id="Evaluation-1"><dummy id="K11-1">K11</dummy><dummy id="K16-1">K16</dummy><dummy id="K57-1">K57</dummy>'
            , unsafe_allow_html=True)
st.markdown('<dummy id="ISP-1"></dummy>', unsafe_allow_html=True)
st.markdown("<h3>Evaluation of current state:</h3>", unsafe_allow_html=True)
st.markdown("<pb>Information Security Policy:</p>", unsafe_allow_html=True)
st.divider()

st.markdown("<h3>Network and security enhancement proposal</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.475, 0.025, 0.5])
with col1:
    st.markdown("<p>Revit is a 3d modelling software (fig 2) widely used across our UK structures team, it constitutes a large portion of our day to day operations and it has been my role in recent years to build scripts and tools to speed up production and automate repetitive tasks, by accessing the software’s API we have built an in house Aecom specific ribbon (fig3) which has been deployed to more than 30 users across the UK, given that the tools have taken time to build it has become important to understand the impact that these tools have had and if the return on investment has been worthwhile, also we want to use these metrics to present to stakeholders in a bid to secure funds for further development. </p>", unsafe_allow_html=True)
    st.markdown("<p>During the last deployment of the tool, I inserted code into each button that writes the telemetry data to a common text file stored on the one-drive. This was a far from optimal, security was a major concern considering everyone had access to the file because they needed write permissions. It also had performance issue as coincident button presses resulted in conflict and temporary file creation fig (4). Considering this data contained personal identifiable information it was also GDPR issue.</p>", unsafe_allow_html=True)
with col3:
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    imageOSI  = Image.open('revit.PNG')
    resized_OSI = imageOSI.resize((1200, 800))
    st.image(resized_OSI, caption='fig 2 - Revit modelling software')
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    imageOSI  = Image.open('Toolbar.PNG')
    resized_OSI = imageOSI.resize((1600, 200))
    st.image(resized_OSI, caption='fig 3 - Aecom in house Toolbar')

    
    imageOSI  = Image.open('Pasted image 20231125121933.png')
    resized_OSI = imageOSI.resize((1200, 300))
    st.image(resized_OSI, caption='fig 4 - Current storage system')
    
st.markdown("<h3></h3>", unsafe_allow_html=True)  
imageOSI  = Image.open('pngfind.com-microsoft-png-1121331.png')
resized_OSI = imageOSI.resize((400, 50))
st.image(resized_OSI)
st.markdown("<p>The obvious answer was to send this data direct to the cloud where it could be controlled by way of role based access. This would require direct transmission of the data from the software api to cloud storage.</p>", unsafe_allow_html=True)
st.markdown("<p>I first needed to decide which type of storage would be suitable, this would depend on the characteristics of the data and the frequency of read/write throughputs.</p>", unsafe_allow_html=True)
st.markdown("<p>Comparing various solutions blob table storage came out on top, this was due to the nature and frequency of the data being stored. Horizontal scaling, a flexible schema and pay as you go pricing model all fit with storing telemetry data types.</p>", unsafe_allow_html=True)
st.markdown("<p>I adapted the code to send json data direct to the blob storage table, however it became apparent that embedding storage account credentials into the code was a security risk, after researching the issue I came to the conclusion that a serverless architecture was the way forward. serverless computing allows the execution of code in response to events without the need for maintaining server infrastructure.</p>", unsafe_allow_html=True)
st.markdown("<p>To better understand the process I created a diagram outlining the route data would take and to better understand the proposed architecture and microservices involved.</p>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True) 

col1, col2, col3 = st.columns([0.3, 0.02, 0.68])
with col1:
    st.markdown("<h3></h3>", unsafe_allow_html=True) 
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.markdown("<h3></h3>", unsafe_allow_html=True) 
    st.markdown("<h3></h3>", unsafe_allow_html=True) 
    st.markdown("<p>Using this system data is sent via the HTTP protocol to an Azure-hosted Function App, which utilises an HTTP trigger to initiate the process. The credentials are verified through Azure Vault, and once authenticated, the Function App processes the data, sending it up to the storage table. All computers send data to the same endpoint, and Azure employs a queue system to process the data sequentially</p>", unsafe_allow_html=True)
with col3:
    st.markdown("<h3></h3>", unsafe_allow_html=True) 
    imageOSI  = Image.open('azurearch.png')
    resized_OSI = imageOSI.resize((800, 600))
    st.image(resized_OSI)
st.markdown("<h3></h3>", unsafe_allow_html=True) 
imageOSI  = Image.open('portalstore.PNG')
resized_OSI = imageOSI.resize((850, 650))
st.image(imageOSI, caption='fig6 - Data in azure portal')

st.markdown("<h3></h3>", unsafe_allow_html=True) 

st.markdown('<pb>Share responsibility model:</pb>', unsafe_allow_html=True)
st.markdown("<p>Once the data is in the cloud fig(6), Cybersecurity is largely handle by Azure as part of their Infrastructure as a service, however as part of the shared responsibility model it is within my remit to handle certain configurations and to make sure that the data is secure in transit, referring back my evaluation of Aecom’s cyber-security policies and the NIST framework I must check for vulnerabilities in my workflow.</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.35, 0.1, 0.55])
with col1:
    st.markdown("<p><pb>Man-in-the-Middle Attacks: </pb>Data transmitted over the internet is susceptible to interception by attackers, who may position themselves between the client and serverless function to eavesdrop or modify data. Configuring request data to be sent via the https protocol and not http ensure end to end encryption. I also ran a port sniff on my endpoint web page to make sure that my TCP/IP port settings adhered to Aecoms Internet Traffic policy.</p>", unsafe_allow_html=True)
with col3:
    imageOSI  = Image.open('portsniff100.PNG')
    resized_OSI = imageOSI.resize((500, 400))
    st.image(resized_OSI)
st.markdown("<p><pb>Distributed Denial of Service (DDoS): </pb>attacks are a malicious attempt to disrupt the normal functioning of a service, or network by overwhelming it with a flood of internet traffic. I configured the function app with a rate limit blocking an Ip address from making too many requests within a certain time frame.</p>", unsafe_allow_html=True)
st.markdown("<p><pb>SQL Injection : </pb>occurs when an attacker injects malicious SQL code into input fields or parameters that are used in a database, as I am using a noSQL table storage I am not so concerned with this but must be aware that noSQL injection attacks do also occur. </p>", unsafe_allow_html=True)

st.markdown("<p><pb>Virtual Private Network: </pb>After releasing a new version of the tool to a select group for beta testing, I hit a hurdled, the SSL/TLS (Secure Sockets Layer/Transport Layer Security) is a protocol to provide secure communication over a network and it was blocking my connection.", unsafe_allow_html=True)
imageOSI  = Image.open('RequestFail.png')
resized_OSI = imageOSI.resize((1200, 100))
st.image(resized_OSI)
st.markdown("<p>Specifically the `ssl_minimum_version` parameter was set to `ssl.TLSVersion.TLSv1`. This parameter is used to specify the minimum SSL/TLS version that should be used when establishing a connection. In this case, it's set to TLSv1, which is an older version of the TLS (Transport Layer Security) protocol. I changed my code to use ssl.TLSVersion.TLSv2 and my connection was restored.</p>", unsafe_allow_html=True)
st.markdown("<p>I understand that this is a particularly technical issue but I feel worth mentioning as it reinforced my confidence that my network was functioning securely.</p>", unsafe_allow_html=True)
st.markdown("<pb>Conclusion: </pb>", unsafe_allow_html=True)
st.markdown("<p>The workflow has proved a huge improvement on the original and has become a proof of concept for further security enhancements and data storage, the attacks listed above are particularly relevant to serverless architecture but are not by any means exhaustive, azure microservices provide good monitoring tools as part of their infrastructure, analysing metrics and logs and setting up alerts and notifications will be ongoing work, application insights will help better understand the behaviour of the data which all go to improving the efficiency, effectiveness and security of aecoms most prizes asset.</p>", unsafe_allow_html=True)

st.divider()
st.markdown("<h3>Impact Story</h3>", unsafe_allow_html=True)