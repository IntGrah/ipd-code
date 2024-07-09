import os
import numpy as np

import simulate
from examples import *

from submissions.FinalShittyStrat_an697 import Strategy as FinalShittyStrat_an697
from submissions.forgiveness_kitten import Strategy as forgiveness_kitten
from submissions.idkWhatImDoingokok import Strategy as idkWhatImDoingokok
from submissions.intgrah import Strategy as intgrah
from submissions.iplsub import Strategy as iplsub
from submissions.jesus import Strategy as jesus
from submissions.Jimboko import Strategy as Jimboko
from submissions.maya_with_flower import Strategy as maya_with_flower
from submissions.MEOWMEOWMEOWMEOWMEOW import Strategy as MEOWMEOWMEOWMEOWMEOW
from submissions.NeelD_titfortatwithatwist2 import Strategy as NeelD_titfortatwithatwist2
from submissions.olifog import Strategy as olifog
from submissions.random_problems import Strategy as random_problems
from submissions.sol4859606_boxy import Strategy as sol4859606_boxy
from submissions.the_cavalry import Strategy as the_cavalry
from submissions.trinityhasstinkywater import Strategy as trinityhasstinkywater
from submissions.yh548 import Strategy as yh548

strategies = [
    TitForTat,
    Grim,
    FinalShittyStrat_an697,
    forgiveness_kitten,
    idkWhatImDoingokok,
    intgrah,
    iplsub,
    jesus,
    Jimboko,
    maya_with_flower,
    MEOWMEOWMEOWMEOWMEOW,
    NeelD_titfortatwithatwist2,
    olifog,
    random_problems,
    sol4859606_boxy,
    the_cavalry,
    trinityhasstinkywater,
    yh548,
]

names = np.array([
    "TitForTat",
    "Grim",
    "FinalShittyStrat_an697",
    "forgiveness_kitten",
    "idkWhatImDoingokok",
    "intgrah",
    "iplsub",
    "jesus",
    "Jimboko",
    "maya_with_flower",
    "MEOWMEOWMEOWMEOWMEOW",
    "NeelD_titfortatwithatwist2",
    "olifog",
    "random_problems",
    "sol4859606_boxy",
    "the_cavalry",
    "trinityhasstinkywater",
    "yh548",
])
n = len(strategies)

scores = np.zeros((n, n), dtype=int)
totals = np.zeros(n, dtype=int)

rs = [5,6,7,8,10,12,13,15,16,18,20,21,24,25,27,28,30,32,35,37,41,44,45,48,49,51,56,60,64,69,72,80,83,89,92,96,101,107,113,121,133,145,151,163,201,241,321,421,513,841]
np.random.shuffle(rs)

assert np.size(rs) == 50
assert np.max(rs) < 1000
assert np.median(rs) == 50
assert np.mean(rs) == 100

for r in rs:
    for i in range(n):
        for j in range(i + 1, n):
            p1 = strategies[i]
            p2 = strategies[j]
            score1, score2 = simulate.simulate(p1(), p2(), r, 0.05)
            scores[i][j] += score1
            scores[j][i] += score2
            
            totals[i] += score1
            totals[j] += score2

indices = np.argsort(-totals)
s_scores = scores[indices, :][:, indices]
s_totals = totals[indices]
s_names = names[indices]

for fn in os.listdir("submissions"):
    if not fn.endswith(".py"):
        continue
    with open(f"submissions/{fn}", "r") as f:
        code = f.read()
    uname = fn.split(".")[0]
    path = f"view/{uname}/"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="/prism.css" rel="stylesheet" />
    <link href="/styles.css" rel="stylesheet" />
    <title>{uname} &ndash; IntGrah</title>
</head>
<body>
    <h1>{uname}</h1>
    <pre class="line-numbers"><code class="language-python">{code}</code></pre>
    <script src="/prism.js"></script>
</body>
</html>""")

with open("leaderboard.html", "w") as f:
    for i, (name, total) in enumerate(zip(s_names, s_totals)):
        f.write(f"<tr>\n  <td>{i+1}</td>\n  <td><a href=\"/submissions/{name}\">{name}</a></td>\n  <td>{total}</td>\n</tr>\n")
    
with open("pairings.html", "w") as f:
    f.write("<tr>\n  <th></th>\n")
    for name in s_names:
        f.write(f"  <th class=\"small\">{name if len(name) < 10 else name[:10]+"…"}</th>\n")
    f.write("</tr>\n")
    for i, (name, scores) in enumerate(zip(s_names, s_scores)):
        f.write(f"<tr>\n  <th><a href=\"/submissions/{name}\">{name}</a></th>\n")
        for score in scores:
            f.write(f"  <td>{score if score else "—"}</td>\n")
        f.write("</tr>\n")
