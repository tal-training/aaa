import Bio.Seq as seq

DATA=""
ANALYSIS=""

def load_file():
    import os
    for i, filename in enumerate(os.listdir()):
        print(i, filename)
    content=f"""
    Choose File Number: 
    """
    choice=int(input(content))
    f=open(os.listdir()[choice])
    global DATA
    DATA=f.read()
    menu(f"MESSAGE: {filename} is loaded")
    
def analyze_data():
    content=f"""
    {DATA}
    Analysis Options:
    ----------------

    1) Translate
    2) Transcribe
    """
    global ANALYSIS
    choice=input(content)
    if choice=="1":
        ANALYSIS=seq.Seq(DATA).translate()
    if choice=="2":
        ANALYSIS=seq.Seq(DATA).transcribe()
    menu(message=f"Result: {ANALYSIS}")


def menu(message=""):
    content=f"""
    {message}
    Choose an Option:
    ----------------

    1) Load Data from File
    2) Load Data from Web
    3) Analyze Data
    4) Save Analysis
    5) Exit
    """
    choice=input(content)
    if choice=="1":
        load_file()
    if choice=="3":
        analyze_data()


menu()