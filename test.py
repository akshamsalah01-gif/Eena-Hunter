import streamlit as st

st.title("Eena Hunter")

# inputting name
name = st.text_input("What is your name? write your GENUINE real name.")

if name:
    st.write(f"Why hello there, **{name}**!")
    
    # Check for 'eena'
    if name.lower() == 'eena':
        st.radio("Are you losing your mind?", ["Yes", "No"], key="eena_radio")
        ans = st.selectbox("Confirm status:", ["yes", "no"], key="eena_select")

        if ans:
            if ans.lower() == "yes":
                st.warning("I knew it!")
            elif ans.lower() == "no":
                st.write("Good for you buddy! Check dms!")
    else:
        st.write("You are not Eena, but that's okay!")
        alt_name = st.text_input("What is your name again?", key="alt_name_input")
        
        if alt_name:
            ans = st.selectbox(
                f"Oh mb {alt_name}, I'm looking for Eena, have you seen her?", 
                ["yes", "no"], 
                index=None, 
                key="eena_seen_select"
            )           
            
            if ans == "yes":
                location = st.text_input("Oh, where is she?", key="loc_input")
                
                if location:
                    loc = location.lower()
                    
                    if any(w in loc for w in ["butt", "booty", "ass", "bottom"]):
                        st.write("I don't think I'll be able to go inside your bottom to find her, please fart her out for me!")
                    elif "toes" in loc or "toe" in loc:
                        st.write("Uhh, I don't think i can go look for her under your toes, please take her out for me!")
                    elif "foot" in loc or "feet" in loc:
                        st.write("I don't think I can go inside OR under your feet to find her, please take her out for me!")
                    elif "idk" in loc or "ion know" in loc or "i dont know" in loc:
                        st.write(f"Ofc you dont know, {alt_name}, but if you see her, please tell her that I'm looking for her!")
                    elif loc == "under there":
                        st.text_input("under wear?", key="underwear_input")
                        st.write("I see...")

                    else:
                        st.write("I see.")
                        counter = st.text_input("Your reply:", key="counter_input")
                        if counter:
                            if counter.lower() in ["no u dont", "no you dont"]:
                                st.write(f"i do see, but you dont, {alt_name}")
                                
            elif ans == "no":
                st.write("Oh, okay. Well, if you see her, please tell her that I'm looking for her!")
                
                                      

       