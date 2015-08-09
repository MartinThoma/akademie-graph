// The nodes for the graph 
var nodes = [ 
	{ id: 0, label: "Name_001", title: "Name: Name_001<br>Major: Public Policy<br>Group: 6<br>Knows: 1 people<br>Known by: 2 people<br>", value: 2, group: 6, color: { border: "#08545E", background: "#84BBBF" }, original_color: { border: "#08545E", background: "#84BBBF" } },
	{ id: 1, label: "Name_002", title: "Name: Name_002<br>Major: Physik + Philosophie<br>Group: 3<br>Knows: 0 people<br>Known by: 0 people<br>", value: 0, group: 3, color: { border: "#E23507", background: "#E89885" }, original_color: { border: "#E23507", background: "#E89885" } },
	{ id: 2, label: "Name_003", title: "Name: Name_003<br>Major: Evangelische Theologie<br>Group: 5<br>Knows: 2 people<br>Known by: 1 people<br>", value: 1, group: 5, color: { border: "#234587", background: "#98B7F4" }, original_color: { border: "#234587", background: "#98B7F4" } },
	{ id: 3, label: "Name_004", title: "Name: Name_004<br>Major: Medizin<br>Group: 5<br>Knows: 1 people<br>Known by: 0 people<br>", value: 0, group: 5, color: { border: "#234587", background: "#98B7F4" }, original_color: { border: "#234587", background: "#98B7F4" } },
	{ id: 4, label: "Name_005", title: "Name: Name_005<br>Major: Geschichte<br>Group: 3<br>Knows: 1 people<br>Known by: 1 people<br>", value: 1, group: 3, color: { border: "#E23507", background: "#E89885" }, original_color: { border: "#E23507", background: "#E89885" } },
	{ id: 5, label: "Name_006", title: "Name: Name_006<br>Major: Medizin<br>Group: 4<br>Knows: 1 people<br>Known by: 2 people<br>", value: 2, group: 4, color: { border: "#552437", background: "#DBA1BB" }, original_color: { border: "#552437", background: "#DBA1BB" } },
]; 


var edges = [
	{ id: 0, from: 2, to: 0, arrows: "to", color: "#234587", original_color: "#234587"},
	{ id: 1, from: 3, to: 0, arrows: "to", color: "#234587", original_color: "#234587"},
	{ id: 2, from: 0, to: 4, arrows: "to", color: "#08545E", original_color: "#08545E"},
	{ id: 3, from: 5, to: 2, arrows: "to", color: "#552437", original_color: "#552437"},
	{ id: 4, from: 4, to: 5, arrows: "to", color: "#E23507", original_color: "#E23507"},
];