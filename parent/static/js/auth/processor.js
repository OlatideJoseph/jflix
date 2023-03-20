var data_validated={};
const validate_input= async (json_data)=>{
	if (json_data['email']){
	}else if(json_data['username']){

	}else if(json_data['name']){

	}else if (json_data['gender']){

	}
}
$(document).ready(function(){
    let form_length=$('form').children().length;
    alert(form_length);
	let jsignup={

	}
	var counter=0;
	function validate_input(field){
		if (field.attr('type')){
			jsignup[field.attr('name')]=field.val()
			console.log(jsignup);
			return "inputs";
			counter ++
		}else if( !field.attr('type')){
			field=field.children('select')
			jsignup[field.attr('name')]=field.val()
			console.log(jsignup);
			return "others";
			counter++;
		}else{
			console.info("incoming messages");
			throw TypeError;
		}
	}
	var btn = $('.field').hide();
	var obj=$('#email-container');
	$('#next-button').click(function(){
		child=obj.children[1];
		if (child.val() == null){
			throw Error;
		}
		counter++;
		if (counter >=7){
			$(this).hide()
			$('input[type="submit"]').show();
		}else if(counter>=1){
			$('#prev-btn').show();
			$(this).show();
		}else{

		}
		if (validate_input(obj.children('input')) == "inputs"){
			var next=obj.next(); //next function for the parent object
			next.toggleClass('field-hidden'); // change the hidden field to the next object
			obj.toggleClass('field-hidden');
			obj=obj.next();
		}else if (validate_input(obj) == "others"){
			obj.toggleClass('field-hidden');
			obj=obj.next();
			obj.toggleClass('field-hidden');
		}
	});
	$('#prev-btn').click(function (){
		child=obj.children[1]
		if (child.val() == null){
			throw Error;
		}
		$('input[type="submit"]').hide();
		if (counter<=1){
            $(this).hide();
            $('#next-button').show();
		}
		counter--;
		obj.toggleClass('field-hidden');
		obj=obj.prev();
		obj.toggleClass('field-hidden');
		$('#next-button').show();
	})
});