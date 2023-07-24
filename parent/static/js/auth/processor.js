'use strict';
$('#send-data').hide();
let universal={
};//variable that stores json object
function validate_object_value(obj){
	let input=obj.children('input').first();
	if (input && input.val()){
		if (input.val()){
			console.log(input.val())
			return true

		}else{
			return false;

		}
	}else if(!input.val()){
		input=obj.children('select').first();
		if (input.val() !== 'None'){
			return true;
		}else{
			return false;
		}
	}else{
		false;
	}
}// validate_object_value ends here
let prev=$('#prev-btn');
let next=$('#next-btn');
let form=$('form').first();
let formlen=$('form').first().children().length;
let count=1;
let formValidated=false;
let obj=$('#email-container');
$().ready(function(){
	prev.click(function(){
		count--;
		if (count == 1){
			prev.hide();
			let n=obj.prev()
			n.show()
			obj.hide()
			obj=n;
			next.show();

		}else if(count > 1 && count <=8){
			let n=obj.prev()
			n.show()
			obj.hide()
			obj=n;
			next.show();

		}
	})
	next.click(function(){
		if (obj.attr('id') == 'email-container'){
			var req;
			console.log(obj.attr('id'))
			$.post(
				`${window.location.origin}/browser/ajax/1.0/user-exist/${obj.children('input').first().val()}/`,
				'email=true',
				function(resp){
					if (resp.user){
						if (!obj.children('p').first().text()){
							let msg=$(
								'<p>A user with that email exists, please give try one.</p>'
							).attr('class','text-error');
							obj.append(msg);
						}
						var req =true;
						return '';
					}
				}
				);
			if (!req)
				return true;
		}
		let validated_outcome=validate_object_value(obj);
		console.log(validated_outcome);
        if (count == 1){
        	if (validated_outcome){
        		let n=obj.next();
        		n.show();
        		obj.hide();
        		prev.show();
        		obj=n
        		count++;// to increase the counts for input
        	};
        	
        }else if( count >1 && count <=8){
        	if (validated_outcome){
        		let n=obj.next();
        		n.show();
        		obj.hide();
        		prev.show();
        		obj=n
        		count++;// to increase the counts for input
        		if (count == 8){
        			next.hide();
        			formValidated=true;
        			$('#send-data').show();
        		}
        	};
        }
	});//click end
});//end
$('#send-data').on('click',function(e){
    e.preventDefault();
    if (formValidated){
    	$.ajax({
		    	url:`${window.location.href}?isajax=true`,
		    	type:'post',
		    	data:$('form').first().serialize(),
		    	success:function(resp){
		    		alert("Form submitted successfully",resp);
		    	},
		    	error:function(){
		    		alert("An error occured !");
		    	}
		});//sends a post request with the serialized data
    }
    
});