import PySimpleGUI as sg

from cblaster.gui.parts import TextLabel


sg.theme("Lightgrey1")


plot_clusters_frame = sg.Frame(
    "Plot Clusters",
    layout=[
        [sg.Text("This module allows for plotting of a subset of clusters using clinker (see citation tab"
                 " for more information). Running clinker using a cblaster session file is significantly"
                 " faster then running clinker with separate genbank files extracted using the Extract"
                 " Clusters module, because the all vs all allignment of clinker can be skipped.",
                 size=(60, 5)
                 )],
        [TextLabel("Session file"),
         sg.InputText(size=(34, 1), key="plot_clusters_session"),
         sg.FileBrowse(key="plot_clusters_session")],
        [sg.Text(
            "A session file (.json) generated by a cblaster search.",
            size=(60, 1)
        )],

        [TextLabel("Output directory"),
         sg.InputText(key="plot_clusters_output", size=(34, 1)),
         sg.FileSaveAs(key="plot_clusters_output")],
        [sg.Text(
            "Directory the final .html file will be saved in.",
            size=(60, 1)
        )],

        [TextLabel("Clusters"), sg.InputText(key="clusters pc")],
        [sg.Text("Cluster numbers/ ranges provided by the summary file of the 'search' command. "
                 "For example to include clusters 1 to 4 use '1-4'. Multiple values can be"
                 " supplied separated by spaces.",
                 size=(60, 3)
                 )],

        [TextLabel("Score threshold"), sg.InputText(key="score threshold pc")],
        [sg.Text("The minimum required score of a cluster in order to be extracted.",
                 size=(60, 1)
                 )],

        [TextLabel("Organisms"), sg.InputText(key="organisms pc")],
        [sg.Text(
            "Organisms that plotted clusters must be from. These take the form"
            " of regular expression patterns and are therefore quite flexible."
            " You can provide more than one pattern."
            " For example, to extract sequences only from Aspergillus and Penicillium"
            " genomes, you might specify: 'Aspergillus.*' 'Penicillium.*'"
            " See the user guide for more examples. Multiple values can be supplied separated by"
            " spaces.",
            size=(60, 5)
        )],

        [TextLabel("Scaffolds"), sg.InputText(key="scaffolds pc")],
        [sg.Text(
            "Scaffolds that plotted clusters must be on. These can be scaffold"
            " names or names AND coordinate ranges. For example, you could specify"
            " scaffold_1, which would retrieve ALL clusters on scaffold_1, or"
            " scaffold_1:10000-50000, which would retrieve only those from position"
            " 10000 to 50000. Multiple values can be supplied separated by spaces.",
            size=(60, 5)
        )],

        [TextLabel("Maximum clusters"), sg.InputText(key="max clusters pc", default_text="50")],
        [sg.Text(
            "The maximum amount of clusters that will be plotted. Ordered on score.",
            size=(60, 1)
        )],
    ],
    title_color="blue",
    font="Arial 10 bold",
    relief="flat",
)

layout = [[plot_clusters_frame]]
