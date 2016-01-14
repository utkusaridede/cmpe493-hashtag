
function loadPanel()
{
}

$('HashtagSegmentorForm').bind('keypress', function(e){
	alert(e.keyCode);
	   if ( e.keyCode == 13 ) {
		   alert('her');
		   segmentHashtag($(HashtagSegmentorForm));
		   return false;
	   }
	 });

$(document).ready(function(){
    $('#hashtag').keypress(function(ev){
      if(ev.keyCode==13){
    	  $('#segmenthashtag').click();
    	  return false;
      }
    });
});

function segmentHashtag(form)
{
	var hashtag = form.hashtag.value.replace("#", "");
	if( hashtag != "" ){
		//var runID = "9ffe742ad9d7d7a97742c87e6b3f0870";
		var runID = "3606e1a6f1e886efdfb19d5192983655";
		var link = "http://79.123.177.134:8081/HashtagSegmentor/"+runID+"/"+hashtag;

		var elmResults = document.getElementById("results");
		elmResults.innerHTML = "Segmenting given hashtag ...";

		var req = createRequest();
		makeRequest(req, link, "", function(){ onSegmentHashtag(req, hashtag); });
	}
}

function onSegmentHashtag(req, hashtag)
{
	if( req.readyState == 4 ){
		var data = req.responseText.replace(/\n/g, ";").replace(/[BI]\t/g, "");
		var json = JSON.parse(data);

		var panel = "";
		panel += "<table width=1100>";
		if( 'segmentation' in json ){
			panel += "<tr><td><b><small>segmentation :</small></b><br><span style='font-size:30px'>"+json['segmentation']+"</span><br><br></td></tr>";
			panel += "<tr><td><b><small>score :</small></b><br>"+json['score']+"</td></tr>";

			if( 'output' in json ){
				var lines = Array();
				var line = strtok(json['output'], ";");
				while(line){
					lines.push(line);
					line = strtok(";");
				}
				panel += "<tr><td><br><b><small>features :</b></small></td></tr>";
				panel += "<tr><td><table width=100%>";
				for(var i = 0; i < lines.length; i++){
					panel += "<tr style='background:#ffffff' height=35><td class=SmallTxt style='line-height:130%' width=20 align=center>"+hashtag[i]+"</td><td class=SmallTxt><small>"+lines[i]+"</small></td></tr>";
				}
				panel += "</table></td></tr>";
			}
			
			if( 'runCode' in json ){
				var runCode = json['runCode'].replace(/;/g, " ");
				panel += "<tr><td><br><br><b><small>run code :</b></small></td></tr>";
				panel += "<tr><td class=SmallTxt style='line-height:140%'><small>"+runCode+"</small></td></tr>";
			}
		}
		else{
			panel += "<tr><td class=SmallTxt><i>no segmentation</i></td></tr>";
		}
		panel += "</table>";

		var elmResults = document.getElementById("results");
		elmResults.innerHTML = panel;
	}
}

function createRequest()
{
	var req;

	// Mozilla, Safari,...
	if( window.XMLHttpRequest ){
		req = new XMLHttpRequest();
		if (req.overrideMimeType)
			req.overrideMimeType('text/xml');
	}
	// IE
	else if( window.ActiveXObject ){
		try {
			req = new ActiveXObject("Msxml2.XMLHTTP");
		}
		catch (e)
		{
			try
			{
				req = new ActiveXObject("Microsoft.XMLHTTP");
			}
			catch (e) {}
		}
	}

	if( !req ){
		alert('Cannot create XMLHTTP instance');
		return false;
	}

	return req;
}

function makeRequest(req, url, parameters, callback)
{
	req.onreadystatechange = callback;
	req.open('GET', url+'?'+parameters, true);
	req.send(null);
}

function strtok (str, tokens) 
{
	this.js_strtok = this.js_strtok || {};

	if( str == undefined )
		return false;
	if (tokens === undefined) {
		tokens = str;
		str = this.js_strtok.strtokleftOver;
	}

	if (str.length === 0) {
		return false;
	}
	if (tokens && str && tokens.indexOf(str.charAt(0)) !== -1) {
		return this.strtok(str.substr(1), tokens);
	}
	for (var i = 0; i < str.length; i++) {
		if (tokens.indexOf(str.charAt(i)) !== -1) {
			break;
		}
	}
	this.js_strtok.strtokleftOver = str.substr(i + 1);
	return str.substring(0, i);
}
