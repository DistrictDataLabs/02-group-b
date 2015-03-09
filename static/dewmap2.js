var width = 1000,
	height = 650;
var statById = d3.map();

var quantile = d3.scale.threshold()
    .domain(isNaN,0,1,5,50)
		.range(['#ffffcc','#a1dab4','#41b6c4','#2c7fb8', '#253494']);
var path = d3.geo.path();
var svg = d3.select("#map")
		.attr("width", width)
		.attr("height", height)
	.append('svg:g');
d3.select("#selectType")
		.on("change", function(){menuChange();});
var tooltip = d3.select("body").append("div")
  	  .attr("class", "tooltip")
  	  .style("opacity", 1e-6)
  	  .style("background", "rgba(250,250,250,.7)");
tooltip.append("span").attr("id", "countyName")
queue()
	.defer(d3.json, "us.json")
	.defer(d3.csv, "mvpfinal020715.csv")
	.defer(d3.json, "countyPop.json")
	.await(ready);
errorArray = [];
var counties;
var countyPop;
function ready(error, us, countiesJSON, countyPopJSON) {
	counties = countiesJSON;
	countyPop = countyPopJSON;
	counties.forEach(function(d){
		try{
			d.lq_11 = +d['lq_11'];
			d.lq_21 = +d['lq_21'];
 			d.lq_22 = +d['lq_22'];
			d.lq_23 = +d['lq_23'];
			d.lq_11 = +d['lq_42'];
			d.lq_11 = +d['lq_51'];
			d.lq_11 = +d['lq_52'];
			d.lq_11 = +d['lq_53'];
      d.lq_11 = +d['lq_55'];
			d.lq_11 = +d['lq_56'];
			d.lq_11 = +d['lq_61'];
			d.lq_11 = +d['lq_62'];
      d.lq_11 = +d['lq_71'];
			d.lq_11 = +d['lq_72'];
			d.lq_11 = +d['lq_81'];
			d.lq_11 = +d['lq_92'];
			statById.set(+d.fips, d);
			if (isNaN(lq_21)) lq_21 = 0;
			if (isNaN(lq_51)) lq_51 = 0;
      {
			}
		}
		catch(e){
			//remove double lines of csv
		}
	});
	countyShapes = svg.append("g")
			.attr("class", "counties")
		.selectAll("path")
			.data(topojson.feature(us, us.objects.counties).features)
		.enter().append("path")
		countyShapes			
			.attr("fill", "rgb(200,200,200)")
			.attr("d", path)
					.on("mouseover", function(d){
						d3.select(this)
							.attr("stroke", "red")
							.attr("stroke-width", 1)
						tooltip
						    .style("left", (d3.event.pageX + 5) + "px")
						    .style("top", (d3.event.pageY - 5) + "px")
						    .transition().duration(300)
						    .style("opacity", 1)
						    .style("display", "block")
						updateDetails(statById.get(d.id));
				})
					.on("mouseout", function(d){
						d3.select(this)
							.attr("stroke", "")
							.attr("stroke-width", .2)
						tooltip.transition().duration(700).style("opacity", 0);
			});
	svg.append("path")
			.datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
			.attr("class", "states")
			.attr("d", path);
	menuChange();
}
var printDetails = [
          {'var': 'fips', 'print': 'FIPS'},
					{'var': 'lq_21', 'print': 'Mining'},
					{'var': 'lq_23', 'print': 'Construction'},
					{'var': 'lq_51', 'print': 'Information'},
          {'var': 'lq_52', 'print': 'Finance, Insurance'},
					{'var': 'lq_61', 'print': 'Education'},
					{'var': 'lq_62', 'print': 'Healthcare'},
					{'var': 'lq_71', 'print': 'Arts and Recreation'}];
function updateDetails(county){
	tooltip.selectAll("div").remove();
	tooltip.selectAll("div").data(printDetails).enter()
		.append("div")
			.append('span')
				.text(function(d){return (d.print.length > 0) ? d.print + ": " : " - ";})				
				.attr("class", "boldDetail")
			.insert('span')
				.text(function(d){
					if (d.var != 'none'){
						return (""+county[d.var]).indexOf('/') == -1 ? totalFormat(county[d.var]) : county[d.var];
					}})
				.attr("class", "normalDetail");
	d3.select("#countyName").text(county.County);
}
var totalFormat = d3.format(",");
function menuChange(){
	var selectType = document.getElementById('selectType');
	selectTypeValue = selectType.options[selectType.selectedIndex].value; 
	var keyName = selectTypeValue;
	console.log(keyName);
	updateMap(keyName);
	console.log(d3.sum(counties, function(d){return d[selectTypeValue];}));
	var num = d3.sum(counties, function(d){return d[selectTypeValue];});
}
function updateMap(key){
	quantile.domain([0,1,5,50]);
	countyShapes
		.transition().duration(1000).ease(d3.ease('linear'))
		.attr("fill", function(d) { 
			if (statById.get(d.id)){
				if(statById.get(d.id)[key] == 0 || statById.get(d.id)[key]== false ){
					return 'white';
				}
				else{
					return quantile(statById.get(d.id)[key]);
				}
			}
			else{
				errorArray.push(d.id);
				return "white";
		}});
}
var ext_color_domain = [0, 1.000, 5.000, 10, 50]
var legend_labels = ["No activity", "Limited activity, <1.0", "Industrial activity, 1-5","Growing activity, 5-50", "Exporter, 50+"]
var colors =(['#ffffcc','#a1dab4','#41b6c4','#2c7fb8', '#253494']);
var legend = svg.selectAll("g.legend")
 .data(ext_color_domain)
 .enter().append("g")
 .attr("class", "legend");
 
var ls_w = 20, ls_h = 25;
 
legend.append("rect")
 .attr("x", 20)
 .attr("y", function(d, i){ return height - (i*ls_h) - 2*ls_h;})
 .attr("width", ls_w)
 .attr("height", ls_h)
 .style("fill", function(d, i) { return colors[i]; } )
 .style("opacity", 0.8);
 
legend.append("text")
 .attr("x", 50)
 .attr("y", function(d, i){ return height - (i*ls_h) - ls_h - 4;})
 .text(function(d, i){ return legend_labels[i]; });


