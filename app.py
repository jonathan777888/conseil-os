from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    response = None

    if request.method == "POST":
        situation = request.form.get("situation", "").strip()

        response = {
            "sage": "Respire. Cette situation mérite d’être regardée avec recul, vérité et patience.",
            "pragmatique": "Identifie une petite action concrète que tu peux faire aujourd’hui sans te mettre trop de pression.",
            "bienveillant": "Tu n’as pas besoin d’être parfait pour avancer. Tu peux apprendre sans te condamner.",
            "protecteur": "Ne prends pas de décision radicale sous le coup de l’émotion. Donne-toi le droit de ralentir.",
            "synthese": f"Tu as partagé : {situation}\n\nConseil OS t’aide à prendre du recul, à agir simplement et à rester bienveillant envers toi-même."
        }

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
