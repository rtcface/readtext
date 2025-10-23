from gtts import gTTS
from pathlib import Path

# Carpeta de salida
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

interviews = {
    "entrevista.mp3": """ 
Hi, my name is Ramiro Tepehua Cortés, and I’m a Full Stack Developer from Tlaxcala, Mexico.
I have over 13 years of experience developing web applications and leading technical projects.

Currently, I work as an Application Development Analyst at SESAET, a government agency. I’ve helped implement the State Digital Platform, which connects with Mexico’s National Digital Platform for public declarations.

My main stack includes Spring Boot, PostgreSQL, Angular, NestJS, MongoDB, and Docker.
I’m passionate about building efficient systems, solving complex problems, and continuously learning new technologies.

I’m now focusing on improving my English so I can collaborate with international teams and take on remote developer roles.

Tell me about yourself

Sure. I started my career over 13 years ago as a web developer, and over time I’ve worked across different environments — from private companies like Amatech, where I also led a development team, to the public sector with SESAET, where I currently work.

At Amatech, I led projects using C# .NET, SQL Server, and Bootstrap, and even managed database permissions and automation processes.
In my current position, I developed and maintained web systems using Java, Spring Boot, and Angular, including features integrated with the National Digital Platform.

I really enjoy collaborating with other developers, learning new frameworks, and building solutions that make processes more efficient.

""",
}

for file, text in interviews.items():
    filepath = output_dir / file
    tts = gTTS(text=text, lang="en")
    tts.save(filepath)
    print(f"✅ Saved: {filepath}")
