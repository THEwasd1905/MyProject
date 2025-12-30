from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return """
  <body style="text-align:center; padding-top:100px; background:#98FB98;">
    <h1>beni seviyor musun?!?</h1>
    <button id="yesBtn"
    onclick="alert('BEN DE SENI SEVIYORUMMM')">
        EVET<3
    </button>

    <br><br>

    <button id="noBtn"
    onmouseover="
    this.style.position='absolute';
    this.style.left=Math.random()*80+'%';
    this.style.top=Math.random()*80+'%';

    let yes = document.getElementById('yesBtn');
    let currentScale = yes.dataset.scale || 1;
    currentScale = parseFloat(currentScale) + 0.5;
    yes.style.transform = 'scale(' + currentScale + ')';
    yes.dataset.scale = currentScale;
    ">
    HAYIR:(
</button>

</body>
</html>
"""
