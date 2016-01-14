<html>
<title>Hashtag Segmentor</title>
<link rel=stylesheet href="index.css" />
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script language="JavaScript" src="segmentor.js"></script>
<body onload='loadPanel()'>
<center>
<table width=1000 style='margin-top:100'>
<tr><td>Enter hashtag to segment: <small>(<i>For English Only</i>)</small></td></tr>
<tr><td align=center>
<form name=HashtagSegmentorForm>
<table><tr>
<td><input id=hashtag style='font-size:25;padding:5px;height:50;width:1000;border:1px solid #cccccc'></td>
<td><input id=segmenthashtag type=button class='blue button' value='Segment' style='font-size:14px;height:50;width:100' onclick='javascript:segmentHashtag(document.HashtagSegmentorForm)'></td>
</tr></table>
</form>
</td></tr>
<tr><td><table width=100%><tr><td id=results></td></tr></table></td></tr>
</table>

</center>
</body>
</html>