import pandas as pd
import random

# -----------------------------
# Human-written style (casual, slang, chatty)
# -----------------------------
human_openers = [
    "Bro, not gonna lie,",
    "Tbh,",
    "Lowkey feeling like",
    "Idk man,",
    "Honestly,",
    "Fr,",
    "No cap,",
    "Brooo,",
    "Dude,",
    "Listen,",
    "Real talk,",
    "Bro fr,",
    "Not even kidding,",
    "Lmao,",
    "Bruh,",
]

human_mid_sentences = [
    "my wifi keeps dying whenever I actually decide to be productive",
    "the app just crashed the exact second I hit save",
    "I was supposed to study but ended up scrolling reels for like two hours",
    "the bus was so crowded I couldn't even move my arm to check my phone",
    "my laptop sounds like a jet engine every time I open VS Code",
    "I made maggi and still somehow managed to burn it",
    "I told myself I’d sleep early but it’s 3am and I’m still awake",
    "I literally forgot why I walked into the kitchen halfway there",
    "I opened my notes and instantly felt sleepy for no reason",
    "my phone was at 5% and of course that’s when everyone decides to call",
    "the power went out right when the match was getting interesting",
    "I saved the file but now I can’t find where I saved it",
    "I joined the online class and the teacher immediately took my name",
    "I kept saying one last episode and somehow finished the whole season",
    "I was so hungry that I finished my food in under five minutes",
]

human_closers = [
    "my life is actually a joke sometimes.",
    "it be like that sometimes fr.",
    "I’m just done at this point.",
    "I really need to get my life together.",
    "and I still act surprised every time.",
    "like why does this always happen to me.",
    "and honestly I only have myself to blame.",
    "I swear the universe is trolling me.",
    "and now I’m just here questioning my decisions.",
    "I need a reset button for real.",
    "and somehow this is becoming my daily routine.",
    "and I'm still pretending everything is fine.",
    "now I’m just staring at the screen like 💀.",
    "I can’t even be mad, this is on me.",
    "I keep saying I'll change, but do I? No.",
]

# Some extra human sentences for variety in paragraphs
human_extra = [
    "My friends keep making plans and cancelling at the last minute.",
    "I keep setting alarms and then snoozing all of them.",
    "The only thing consistent about me is my inconsistency.",
    "Every time I say 'from tomorrow', that tomorrow never comes.",
    "Sometimes I open WhatsApp and forget why I opened it.",
    "I’ll complain about being tired but still stay up late on my phone.",
    "Half my day is just me thinking about what to eat next.",
    "I was supposed to drink more water this week, but here we are.",
    "I keep saying I’ll start going to the gym ‘next Monday’.",
    "My screen time report is basically judging my whole existence.",
]

def generate_human_paragraph():
    # 2–4 sentences
    num_sentences = random.randint(2, 4)
    sentences = []
    for _ in range(num_sentences):
        opener = random.choice(human_openers)
        mid = random.choice(human_mid_sentences)
        close = random.choice(human_closers)
        sentences.append(f"{opener} {mid}, {close}")
    # Optionally add one extra line
    if random.random() < 0.6:
        sentences.append(random.choice(human_extra))
    return " ".join(sentences)


# -----------------------------
# AI-style text (multiple tones)
# -----------------------------

# Formal / academic tone
ai_formal_starters = [
    "This project aims to explore",
    "The primary objective of this system is to demonstrate",
    "In recent years, researchers have increasingly focused on",
    "The rapid growth of artificial intelligence has significantly influenced",
    "From a technical perspective, it is important to understand",
]

ai_formal_mids = [
    "how machine learning models can distinguish between human-written and AI-generated content",
    "the broader implications of deploying automated language models at scale",
    "various strategies for improving classification accuracy on real-world datasets",
    "the role of natural language processing in modern software applications",
    "the challenges associated with maintaining fairness, privacy, and reliability",
]

ai_formal_ends = [
    "in order to build more transparent and trustworthy AI systems.",
    "which may assist organizations in making informed decisions.",
    "and this work contributes to the growing body of research on AI safety.",
    "thus highlighting the importance of robust evaluation pipelines.",
    "which ultimately benefits both developers and end users.",
]

# Explanatory / tutorial tone
ai_explain_starters = [
    "To understand how this model works, consider the following process:",
    "The classification pipeline can be broken down into several steps:",
    "At a high level, the system follows this workflow:",
    "The detection mechanism relies on a simple but effective approach:",
    "You can think of the entire model as a sequence of stages:",
]

ai_explain_mids = [
    "first, the raw text is tokenized and converted into numerical sequences",
    "then, these sequences are padded to a consistent length to form batches",
    "next, the encoded text is passed through an embedding layer followed by an LSTM network",
    "after feature extraction, a dense layer with a sigmoid activation computes the final probability",
    "finally, the output is interpreted as either AI-generated or human-generated text",
]

ai_explain_ends = [
    "this makes the model suitable for real-time applications with moderate resource usage.",
    "overall, the pipeline is straightforward to implement using modern deep learning libraries.",
    "as a result, developers can integrate the classifier into existing web applications.",
    "which allows the system to deliver predictions with minimal latency.",
    "thereby creating a practical tool for educational and experimental purposes.",
]

# Marketing / product tone
ai_marketing_starters = [
    "Our AI-powered detector provides a seamless way to",
    "With this intelligent system, users can effortlessly",
    "Designed for modern creators, this tool helps you",
    "Whether you're a student, teacher, or developer, this application lets you",
    "Built with performance in mind, the platform enables you to",
]

ai_marketing_mids = [
    "analyze written content and determine whether it was generated by a human or an AI model",
    "gain deeper insights into the authenticity of text appearing in your documents or projects",
    "quickly evaluate multiple samples of writing without manual inspection",
    "enhance your workflow by adding a simple layer of AI-generated content detection",
    "improve transparency when sharing or reviewing AI-assisted writing",
]

ai_marketing_ends = [
    "so you can stay confident about the origin of your text.",
    "without needing any prior expertise in machine learning.",
    "in just a few clicks directly from your browser.",
    "while maintaining an intuitive and user-friendly interface.",
    "making AI more accessible and understandable for everyone.",
]

# Extra AI sentences to enrich paragraphs
ai_extra = [
    "The interface can be customized to match different design preferences.",
    "Future updates may include support for additional languages and domains.",
    "The underlying architecture can be extended using transformer-based models.",
    "Careful dataset curation remains essential for achieving reliable outcomes.",
    "Logging and monitoring are recommended when deploying the system in production.",
    "Users are encouraged to provide feedback to continuously improve the tool.",
    "Hybrid approaches that combine rules and machine learning may further boost performance.",
    "This classifier serves as a starting point for exploring responsible AI practices.",
    "Integration with existing authentication systems can help secure access to the tool.",
    "The overall design focuses on balancing accuracy, usability, and efficiency.",
]

def generate_ai_paragraph():
    num_sentences = random.randint(2, 4)
    sentences = []

    # Mix tones: formal, explanation, marketing
    for _ in range(num_sentences):
        tone = random.choice(["formal", "explain", "marketing"])
        if tone == "formal":
            s = f"{random.choice(ai_formal_starters)} {random.choice(ai_formal_mids)}, {random.choice(ai_formal_ends)}"
        elif tone == "explain":
            s = f"{random.choice(ai_explain_starters)} {random.choice(ai_explain_mids)}, {random.choice(ai_explain_ends)}"
        else:  # marketing
            s = f"{random.choice(ai_marketing_starters)} {random.choice(ai_marketing_mids)}, {random.choice(ai_marketing_ends)}"
        sentences.append(s)

    # Optionally add an extra informational sentence
    if random.random() < 0.7:
        sentences.append(random.choice(ai_extra))

    return " ".join(sentences)


# -----------------------------
# Generate dataset
# -----------------------------
num_samples = 1000   # total rows
half = num_samples // 2

rows = []

# 50% human (label = 0), 50% AI (label = 1)
for _ in range(half):
    rows.append([generate_human_paragraph(), 0])
    rows.append([generate_ai_paragraph(), 1])

# Shuffle rows so labels are mixed
random.shuffle(rows)

df = pd.DataFrame(rows, columns=["text", "label"])

# Save CSV – you can change this path if you want
csv_filename = "ai1.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")

print(f"Dataset created: {csv_filename}")
print("Total rows:", len(df))
print(df.head())
