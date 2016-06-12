$(function(){
	var Rows = $("#dataTables-example_wrapper");
	$("#cancel").click(function(){
		$("#close9").click();
	});
	$("#cutorder").click(function(){
		var checkeds = $("input[name='getid']");
		var stat = $("input[name='status']");
		var cutids = new Array();
		for(var i=0;i<checkeds.length;i++){
			if(checkeds[i].checked){
				if (stat[i].value!=11){
					if(stat[i]!=10){
						alert("砍单状态必须是代付款或者代发货");
						return 0;
					};
				};
				cutids.push(checkeds[i].value);
			};
		};
		if(cutids.length==0){		alert("请选择要砍掉的订单号");	return 0;	};
		$("#orders").val(cutids.join("|"));
		var objo = $("select[name='select0']");
		var objt = $("select[name='select1']");
		var objh = $("input[name='subject']");
		var more = "";
		for(var i=0;i<objo.length;i++){
			if(objo[i].value != '-1'){
				more +=  objo[i].value + "|" + objt[i].value + "|" + String(objh[i].value) +"||";
			};
		};
		if (more.length==0){		more="no_con";		};
		$("#querys").val(more);
		$("#cutid").click();
		
	});

	$("#addcon").click(function(){
		var TopDiv = $('<div></div>');
		TopDiv.addClass("row");
		TopDiv.prependTo(Rows);
		var CloneDiv=$("#rows1").clone();
		CloneDiv.find("select").each(function(){
			$(this).val(-1);
		});
		CloneDiv.find("input").each(function(){
			$(this).val("");
			$(this).attr("placeholder","");
		});
		CloneDiv.attr('id',Math.random().toString());
		CloneDiv.appendTo(TopDiv);
		var MidDiv = $('<div></div>');
		MidDiv.addClass('col-sm-6');
		MidDiv.appendTo(TopDiv)
		var MSDiv = $('<div></div>');
		MSDiv.addClass('dataTables_filter');
		MSDiv.attr('id',"dataTables-example_filter");
		MSDiv.appendTo(MidDiv);
		var Label = $('<label></label>');
		Label.appendTo(MSDiv);
		var Cancel=$('<input />');
		Cancel.attr('type','reset');
		Cancel.attr('value','-');
		Cancel.click(function(){$(this).parent().parent().parent().parent().remove()});
		Cancel.addClass('btn');
		Cancel.appendTo(Label);
	});
	$("#query").click(function(){
			var objo = $("select[name='select0']");
			var objt = $("select[name='select1']");
			var objh = $("input[name='subject']");
			var more = "";
			for(var i=0;i<objo.length;i++){
				if(objo[i].value != '-1'){
					more +=  objo[i].value + "|" + objt[i].value + "|" + String(objh[i].value) +"||";
				};
			};
			if (more.length>0){		more="?&op=" + more;		};
			window.location.href = window.location.pathname + more;
	});

	$(document).on("click","ul[class='pagination pagination-sm'] li a",function(){
			var objo = $("select[name='select0']");
			var objt = $("select[name='select1']");
			var objh = $("input[name='subject']");
			var more = "";
			for(var i=0;i<objo.length;i++){
				if(objo[i].value != '-1'){
					more +=  objo[i].value + "|" + objt[i].value + "|" + String(objh[i].value) +"||";
				};
			};
			if (more.length>0){		more="&op=" + more;		};
			if ($(this).attr('href')=="#"){	$(this).attr('href',window.location.pathname + '?' + more);	}
			else{	$(this).attr('href',$(this).attr('href')+ more); 								};
			
	});
});
