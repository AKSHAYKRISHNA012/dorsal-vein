import streamlit as st

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)



authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login()

# if username.isdigit():
#     st.error('Username not be Numbers')
if authentication_status == False:
    st.error('Username/password is incorrect')
if authentication_status == None:
    st.warning('Please enter your username and password')
if authentication_status:
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}")
        st.title('Dorsal Hand Vein-Based Authentication System')

        st.sidebar.header('Devoleped By')
        st.sidebar.write('- Akshay Krishna A')
        st.sidebar.write('- Adiya Sneha Simon')
        st.sidebar.write('- Abhin Krisha M B')
        st.sidebar.write('- Aswathy P A')

        st.write()
        st.write("""<div style="font-size:20px;">In recent years, biometric authentication systems have gained significant attention due to their reliability
                and security in verifying individuals' identities. Among various biometric modalities, dorsal hand vein-based authentication has emerged as a  
                promising approach, offering unique advantages such as high accuracy, non-invasiveness, and resistance to 
                spoofing attacks. This paper proposes a novel dorsal hand vein-based authentication system that utilizes 
                near-infrared imaging technology to capture vein patterns beneath the skin's surface. The proposed system employs advanced 
                image processing techniques to extract and analyze the unique vein patterns, which are then used to authenticate individuals.
                Experimental results on a dataset of dorsal hand vein images demonstrate the effectiveness and robustness of the proposed 
                authentication system, achieving high accuracy and low false acceptance rates. Furthermore, the system's non-invasive nature  
                and ease of deployment make it suitable for various applications, including access control, identity verification, 
                and secure authentication in both physical and digital environments. Overall, the proposed dorsal hand vein-based authentication
                system presents a promising solution for enhancing security and privacy in biometric authentication systems.</div>""", unsafe_allow_html=True)
        


st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

if authentication_status is None:
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
        if username_of_registered_user and name_of_registered_user:
            if username_of_registered_user.isdigit() or name_of_registered_user.isdigit():
                st.error("Username and name cannot consist only of numbers.")
            else:
                st.success('User registered successfully')
        else:
            st.warning("Fill in all the Details")
    except Exception as e:
        st.error(e)

with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)