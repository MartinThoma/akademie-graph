// The nodes for the graph 
var nodes = [ 
	{ id: 0, label: "Name_001", title: "Name: Name_001<br>Major: Public Policy<br>Group: 6<br>Knows: 1 people<br>Known by: 2 people<br>", value: 2, group: 6, color: { border: "rgb(255, 215, 0)", background: "rgb(255, 227, 77)", highlight:{ border: "rgb(255, 215, 0)", background: "rgb(255, 227, 77)" } }, original_color: { border: "rgb(255, 215, 0)", background: "rgb(255, 227, 77)", highlight: { border: "rgb(255, 215, 0)", background: "rgb(255, 227, 77)" } }, hiking: 1 },
	{ id: 1, label: "Name_002", title: "Name: Name_002<br>Major: Physik + Philosophie<br>Group: 3<br>Knows: 2 people<br>Known by: 0 people<br>", value: 0, group: 3, color: { border: "rgb(100, 149, 237)", background: "rgb(146, 181, 242)", highlight:{ border: "rgb(100, 149, 237)", background: "rgb(146, 181, 242)" } }, original_color: { border: "rgb(100, 149, 237)", background: "rgb(146, 181, 242)", highlight: { border: "rgb(100, 149, 237)", background: "rgb(146, 181, 242)" } }, hiking: 2 },
	{ id: 2, label: "Name_003", title: "Name: Name_003<br>Major: Evangelische Theologie<br>Group: 5<br>Knows: 0 people<br>Known by: 1 people<br>", value: 1, group: 5, color: { border: "rgb(34, 139, 34)", background: "rgb(100, 174, 100)", highlight:{ border: "rgb(34, 139, 34)", background: "rgb(100, 174, 100)" } }, original_color: { border: "rgb(34, 139, 34)", background: "rgb(100, 174, 100)", highlight: { border: "rgb(34, 139, 34)", background: "rgb(100, 174, 100)" } }, hiking: 2 },
	{ id: 3, label: "Name_004", title: "Name: Name_004<br>Major: Medizin<br>Group: 5<br>Knows: 1 people<br>Known by: 0 people<br>", value: 0, group: 5, color: { border: "rgb(34, 139, 34)", background: "rgb(100, 174, 100)", highlight:{ border: "rgb(34, 139, 34)", background: "rgb(100, 174, 100)" } }, original_color: { border: "rgb(34, 139, 34)", background: "rgb(100, 174, 100)", highlight: { border: "rgb(34, 139, 34)", background: "rgb(100, 174, 100)" } }, hiking: 0 },
	{ id: 4, label: "Name_005", title: "Name: Name_005<br>Major: Geschichte<br>Group: 3<br>Knows: 1 people<br>Known by: 2 people<br>", value: 2, group: 3, color: { border: "rgb(100, 149, 237)", background: "rgb(146, 181, 242)", highlight:{ border: "rgb(100, 149, 237)", background: "rgb(146, 181, 242)" } }, original_color: { border: "rgb(100, 149, 237)", background: "rgb(146, 181, 242)", highlight: { border: "rgb(100, 149, 237)", background: "rgb(146, 181, 242)" } }, hiking: 1 },
	{ id: 5, label: "Name_006", title: "Name: Name_006<br>Major: Medizin<br>Group: 4<br>Knows: 1 people<br>Known by: 1 people<br>", value: 1, group: 4, color: { border: "rgb(230, 126, 0)", background: "rgb(238, 165, 77)", highlight:{ border: "rgb(230, 126, 0)", background: "rgb(238, 165, 77)" } }, original_color: { border: "rgb(230, 126, 0)", background: "rgb(238, 165, 77)", highlight: { border: "rgb(230, 126, 0)", background: "rgb(238, 165, 77)" } }, hiking: 0 },
]; 


var edges = [
	{ id: 0, from: 1, to: 0, arrows: "to", color: "rgb(100, 149, 237)", original_color: "rgb(100, 149, 237)"},
	{ id: 1, from: 1, to: 4, arrows: "to", color: "rgb(100, 149, 237)", original_color: "rgb(100, 149, 237)"},
	{ id: 2, from: 4, to: 2, arrows: "to", color: "rgb(100, 149, 237)", original_color: "rgb(100, 149, 237)"},
	{ id: 3, from: 3, to: 4, arrows: "to", color: "rgb(34, 139, 34)", original_color: "rgb(34, 139, 34)"},
	{ id: 4, from: 5, to: 0, arrows: "to", color: "rgb(230, 126, 0)", original_color: "rgb(230, 126, 0)"},
];