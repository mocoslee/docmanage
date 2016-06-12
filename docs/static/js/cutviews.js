$(function(){

	$("#info").click(function(){
		$("#cutid").click();
	
	});
	$("#loadout").click(function(){
		var subject = $("#subject").val();
		if(subject.length==0){
			alert("请输入要导出的批次号");
			$("#subject").focus();
			return 0;
		};
		
		url = '/userauth/loadout?subject='+subject;
		window.open(url);
	});

	$("#warning").click(function(){
		var stat = $("#select0").val();
		if (stat!=0){
			alert("要终止的任务必须是待执行状态");
			return 0;
		};
		
		
	});

	$("#query").click(function(){
			var objo = $("select[name='select0']");
			var objh = $("input[name='subject']");
			var more = "";
			for(var i=0;i<objo.length;i++){
				if(objo[i].value != '-1'){
					more =  "&status=" + objo[i].value ;
				};
				if(objh[i].value){
					more += "&op_time=" + String(objh[i].value);
				};
			};

			window.location.href = window.location.pathname + '?' +  more;
	});

	$(document).on("click","ul[class='pagination pagination-sm'] li a",function(){
			var objo = $("select[name='select0']");
			var objh = $("input[name='subject']");
			var more = "";
			for(var i=0;i<objo.length;i++){
				if(objo[i].value != '-1'){
					more =  "&status=" + objo[i].value ;
				};
				if(objh[i].value){
					more += "&op_time=" + String(objh[i].value);
				};
			};
			if ($(this).attr('href')=="#"){	$(this).attr('href',window.location.pathname + '?' + more);	}
			else{	$(this).attr('href',$(this).attr('href')+ more); 								};
			
	});
	
});
