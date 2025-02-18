import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for the floating mascot and chat interface
st.markdown("""
<style>
.mascot-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    cursor: pointer;
    transition: opacity 0.3s;
    opacity: 0.7;
}

.mascot-container:hover {
    opacity: 1;
}

.mascot-image {
    width: 100px;
    height: 100px;
}

.tooltip {
    position: absolute;
    top: -40px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #333;
    color: white;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 12px;
    white-space: nowrap;
    display: none;
}

.mascot-container:hover .tooltip {
    display: block;
}

.chat-container {
    position: fixed;
    bottom: 140px;
    right: 20px;
    width: 300px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    z-index: 999;
    display: none;
}
</style>
""", unsafe_allow_html=True)

# JavaScript for handling click events and chat visibility
js_code = """
<script>
function toggleChat() {
    const chat = document.querySelector('.chat-container');
    if (chat.style.display === 'none' || chat.style.display === '') {
        chat.style.display = 'block';
    } else {
        chat.style.display = 'none';
    }
}
</script>
"""

# HTML structure for the mascot and chat interface
html_code = f"""
<div class="mascot-container" onclick="toggleChat()">
    <div class="tooltip">Click me for orientation Q&A</div>
    <img src="path_to_your_mascot_image.png" class="mascot-image" alt="Mascot">
</div>
<div class="chat-container">
    <div style="padding: 15px;">
        <h3>Orientation Q&A</h3>
        <div id="chat-messages" style="height: 300px; overflow-y: auto;">
            <!-- Chat messages will appear here -->
        </div>
    </div>
</div>
{js_code}
"""

# Main Streamlit app
def main():
    st.title("JCU Singapore")
    
    # Add your main content here
    st.write("Welcome to James Cook University Singapore!")
    
    # Inject the HTML/CSS/JS code
    components.html(html_code, height=0)
    
    # Add chat functionality using Streamlit
    if 'messages' not in st.session_state:
        st.session_state.messages = []

if __name__ == "__main__":
    main()
