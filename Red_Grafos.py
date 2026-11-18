pos = {
    "CIA": (0, 1.5),
    "RM": (2.5, 2.8),
    "PC": (5, 2.2),
    "MA": (5, 0.2),
    "MB": (7.5, 2.2),
    "MG": (8.8, 0.2)
}

colores = {
    "CIA": "#2878B5",
    "RM": "#8264A6",
    "PC": "#239B69",
    "MA": "#C94C4C",
    "MB": "#C94C4C",
    "MG": "#C94C4C"
}

plt.figure(figsize=(11, 6))

nx.draw_networkx_nodes(
    G, pos,
    node_size=2500,
    node_color=[colores[n] for n in G.nodes()],
    edgecolors="white",
    linewidths=2.5
)

nx.draw_networkx_labels(
    G, pos,
    font_size=12,
    font_weight="bold",
    font_color="white"
)

nx.draw_networkx_edges(
    G, pos,
    arrows=True,
    arrowsize=20,
    width=1.7,
    connectionstyle="arc3,rad=0.0",
    edge_color="#596579",
    min_source_margin=23,
    min_target_margin=25
)

pesos = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=pesos,
    font_size=10,
    bbox=dict(
        boxstyle="round,pad=0.18",
        fc="white",
        ec="#D6DEE8"
    )
)

plt.title(
    "Red de Transferencia Tecnológica para MiPymes",
    fontsize=14,
    fontweight="bold"
)

plt.figtext(
    0.5, 0.02,
    "Azul: Centro IA | Morado: Mentores | Verde: Parque científico | Rojo: MiPymes",
    ha="center",
    fontsize=9
)

plt.axis("off")
plt.tight_layout()
plt.show()
