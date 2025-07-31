import os
from dotenv import load_dotenv
import google.generativeai as genai
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Menu banner
def print_menu():
    print(Fore.CYAN + "\n🎓 Smart Student Assistant")
    print(Fore.YELLOW + "📘 Available Commands:")
    print(Fore.GREEN + "   tip" + Fore.WHITE + "               → Get a study tip")
    print(Fore.GREEN + "   summarize: <text>" + Fore.WHITE + " → Summarize a passage")
    print(Fore.GREEN + "   define: <term>" + Fore.WHITE + "   → Define an academic term")
    print(Fore.GREEN + "   translate: urdu: <text>" + Fore.WHITE + " → Translate to Urdu")
    print(Fore.GREEN + "   help" + Fore.WHITE + "              → Show this menu again")
    print(Fore.RED + "   exit" + Fore.WHITE + "              → Quit assistant\n")

# Initial welcome
print_menu()

# Conversation loop
while True:
    user_input = input(Fore.BLUE + "🧑‍🎓 You: " + Style.RESET_ALL).strip()

    if not user_input:
        print("🤖 Assistant: Please enter something!\n")
        continue

    if user_input.lower() in ["exit", "quit"]:
        print(Fore.MAGENTA + "👋 Assistant: Stay curious! Goodbye.\n")
        break

    if user_input.lower() == "help":
        print_menu()
        continue

    # Handle different commands
    if user_input.lower() == "tip":
        prompt = "Give me a practical and motivational study tip for students."

    elif user_input.lower().startswith("summarize:"):
        content = user_input[len("summarize:"):].strip()
        if len(content.split()) < 5:
            print("📏 Please provide a slightly longer text to summarize.\n")
            continue
        prompt = f"Summarize this text clearly:\n{content}"

    elif user_input.lower().startswith("define:"):
        term = user_input[len("define:"):].strip()
        prompt = f"Define the academic term: {term}"

    elif user_input.lower().startswith("translate: urdu:"):
        text = user_input.replace("translate: urdu:", "").strip()
        prompt = f"Translate this to Urdu: {text}"

    else:
        prompt = f"Answer this academic question in a helpful tone:\n{user_input}"

    # Get response from Gemini
    try:
        response = model.generate_content(prompt)
        print(Fore.LIGHTGREEN_EX + "🤖 Assistant:", response.text.strip(), "\n")
    except Exception as e:
        print(Fore.RED + f"⚠️ Error: {e}\n")
