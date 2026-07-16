"""Generate slide-native figures for the 'Overview of Outcomes' deck.
Illustrative data built to match the published patterns in Schrag et al. 2022
(Front Vet Sci) and Apley et al. 2023. Run with the project's Python 3.12.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "figs")
os.makedirs(OUT, exist_ok=True)

# ---- palette (ICASA) ----
SLATE="#34495E"; COPPER="#C0693B"; INK="#1F2937"; MUTED="#64748B"; GRID="#E5E9EF"
SUCCESS="#2F7D5B"; RELAPSE="#D98B3A"; SOLD="#6B8AA0"; DIED="#9B2D30"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 15,
    "text.color": INK, "axes.edgecolor": "#B9C4CF",
    "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.linewidth": 1.0, "figure.dpi": 200, "savefig.dpi": 200,
    "savefig.bbox": "tight", "savefig.facecolor": "white", "figure.facecolor": "white",
})

def strip(ax, keep=("left","bottom")):
    for s in ("top","right","left","bottom"):
        ax.spines[s].set_visible(s in keep)

# =====================================================================
# FIGURE A — Outcome decomposition: same success %, opposite failure story
# =====================================================================
def fig_decomposition():
    cats = ["Success","Relapse","Sold","Died"]
    cols = [SUCCESS,RELAPSE,SOLD,DIED]
    # Blue Dairy: low success driven by DEATH ; Yellow Dairy: driven by RELAPSE+CULL
    data = {
        "Blue Dairy":   [66, 5, 4, 25],
        "Yellow Dairy": [66, 22, 10, 2],
    }
    farms = list(data.keys())
    fig, ax = plt.subplots(figsize=(10.2, 3.5))
    ypos = [1.0, 0.0]
    for yi, farm in zip(ypos, farms):
        left = 0
        for val, c, name in zip(data[farm], cols, cats):
            ax.barh(yi, val, left=left, height=0.52, color=c, edgecolor="white", linewidth=1.2)
            if val >= 6:
                ax.text(left+val/2, yi, f"{val}", ha="center", va="center",
                        color="white", fontsize=13, fontweight="bold")
            left += val
    ax.set_yticks(ypos); ax.set_yticklabels(farms, fontsize=15, fontweight="bold", color=INK)
    ax.set_xlim(0,138); ax.set_xlabel("% of therapeutic events (30-day outcome)", color=MUTED, fontsize=12.5)
    strip(ax, keep=("bottom",))
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([0,25,50,75,100]); ax.set_xticklabels(["0","25","50","75","100"], fontsize=11)
    # bracket annotation over the shared success level
    ax.annotate("same 66% success", xy=(33,1.0), xytext=(33,1.66), ha="center",
                fontsize=12.5, color=SLATE, fontweight="bold")
    ax.annotate("", xy=(33,0.30), xytext=(33,1.5),
                arrowprops=dict(arrowstyle="-", color=SLATE, lw=1, ls=":"))
    # failure-driver callouts OUTSIDE the bars (right margin)
    ax.text(104, 1.0, "failure driver:\nDEATH", ha="left", va="center", color=DIED, fontsize=11.5, fontweight="bold")
    ax.text(104, 0.0, "failure driver:\nRELAPSE + culling", ha="left", va="center", color=RELAPSE, fontsize=11.5, fontweight="bold")
    ax.set_ylim(-0.6, 2.0)
    # legend
    handles=[plt.Rectangle((0,0),1,1,color=c) for c in cols]
    ax.legend(handles, cats, ncol=4, loc="lower left", bbox_to_anchor=(0.0,-0.46),
              frameon=False, fontsize=11.5, handlelength=1.1, columnspacing=1.4)
    fig.savefig(os.path.join(OUT,"fig_decomposition.png"))
    plt.close(fig)

# =====================================================================
# FIGURE B — "A single number lies": same yards, different rank by metric
# =====================================================================
def fig_single_number():
    metrics = ["Reg / AY", "mg / kg", "DDD /\n100 hd-days"]
    yards = ["d","i","k","m","o","f"]
    ranks = {  # rank 1 = lowest use ... 6 = highest use
        "d":[1,6,4], "i":[2,3,2], "k":[3,2,5],
        "m":[4,1,6], "o":[5,4,1], "f":[6,5,3],
    }
    highlight = {"d":COPPER, "m":SLATE}
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    x=[0,1,2]
    for y in yards:
        c = highlight.get(y, "#C3CDD6")
        lw = 3.2 if y in highlight else 1.6
        z = 3 if y in highlight else 1
        ax.plot(x, ranks[y], "-o", color=c, lw=lw, markersize=9,
                markerfacecolor=c, markeredgecolor="white", zorder=z)
        ax.text(-0.06, ranks[y][0], y, ha="right", va="center",
                fontsize=13, fontweight="bold", color=c if y in highlight else MUTED)
        ax.text(2.06, ranks[y][2], y, ha="left", va="center",
                fontsize=13, fontweight="bold", color=c if y in highlight else MUTED)
    ax.set_xticks(x); ax.set_xticklabels(metrics, fontsize=13, color=INK)
    ax.set_yticks([1,6]); ax.set_yticklabels(["lowest\nuse","highest\nuse"], fontsize=11.5)
    ax.set_ylim(6.6,0.4); ax.set_xlim(-0.35,2.35)
    strip(ax, keep=())
    ax.tick_params(length=0)
    ax.annotate("Yard d: lowest use by one metric,\nhighest by another",
                xy=(1,6), xytext=(0.55,4.2), fontsize=12.5, color=COPPER, fontweight="bold")
    fig.savefig(os.path.join(OUT,"fig_single_number.png"))
    plt.close(fig)

# =====================================================================
# FIGURE C — Trend within farm context (Red Dairy, metritis)
# =====================================================================
def fig_within_farm():
    years=[2016,2017,2018,2019]
    success=[96,94,89,90]
    incidence=[31,20,9,6]
    fig, (ax1,ax2)=plt.subplots(1,2,figsize=(10.6,4.0),gridspec_kw={"wspace":0.28})

    # panel 1: success with quintile bands
    bands=[(95,101,"top quintile"),(90,95,""),(85,90,""),(80,85,""),(60,80,"bottom")]
    shades=["#DCEAE2","#E9F0EC","#F1F0EC","#F3E9E5","#F6E2E1"]
    for (lo,hi,lab),sh in zip(bands,shades):
        ax1.axhspan(lo,hi,color=sh,zorder=0)
    ax1.plot(years,success,"-o",color=SLATE,lw=3,markersize=10,
             markerfacecolor=SLATE,markeredgecolor="white",zorder=3)
    for x,y in zip(years,success):
        ax1.text(x,y+1.2,f"{y}%",ha="center",fontsize=12,fontweight="bold",color=SLATE)
    ax1.annotate("top quintile", xy=(2016,96), xytext=(2016.05,99.2), fontsize=10.5, color=SUCCESS, fontweight="bold")
    ax1.annotate("near bottom", xy=(2018,89), xytext=(2017.5,84.5), fontsize=10.5, color=DIED, fontweight="bold")
    ax1.set_ylim(80,101); ax1.set_xticks(years); ax1.set_xticklabels(years,fontsize=11)
    ax1.set_title("Therapeutic success",fontsize=13.5,color=INK,fontweight="bold",loc="left")
    ax1.set_ylabel("% success",color=MUTED,fontsize=11.5)
    strip(ax1,keep=("left","bottom"))

    # panel 2: disease incidence bars
    ax2.bar(range(len(years)),incidence,color=COPPER,width=0.62,edgecolor="white")
    for i,v in enumerate(incidence):
        ax2.text(i,v+0.6,str(v),ha="center",fontsize=12,fontweight="bold",color=COPPER)
    ax2.set_xticks(range(len(years))); ax2.set_xticklabels(years,fontsize=11)
    ax2.set_ylim(0,35)
    ax2.set_title("Disease pressure",fontsize=13.5,color=INK,fontweight="bold",loc="left")
    ax2.set_ylabel("therapeutic events / 100 cow-yr",color=MUTED,fontsize=10.5)
    ax2.annotate("prevention win\n(not neglect)", xy=(3,6), xytext=(1.4,24),
                 fontsize=11.5,color=SLATE,fontweight="bold",
                 arrowprops=dict(arrowstyle="->",color=SLATE,lw=1.4))
    strip(ax2,keep=("left","bottom"))
    fig.savefig(os.path.join(OUT,"fig_within_farm.png"))
    plt.close(fig)

fig_decomposition()
fig_single_number()
fig_within_farm()
print("Figures written to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)
