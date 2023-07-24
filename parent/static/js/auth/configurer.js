$(document).ready(function(){
     		$('#form-post');
     		$('#close').click(function(){
				$(this).parent().parent().hide();
			});//closes the page alert!
});


$('form').on('submit',function(e){
        let username = document.querySelector('.username');
        let url=`${window.location.origin}/browser/ajax/1.0/user-exist/`
        let value=$(this).val();
        $.post(url+value,data=value,callback=function(a){
            let span=$('.text-error');
            if(a){
                if (a['code'] =='success'){
                    span.fadeOut(500);
                    return true;
                }else{
                    span.fadeIn(500);
                    span.html(a['message'])
                    e.preventDefault();
                    console.log("this");
                    return false;
                }
            }
        });//validates the username
//     let form=$(this);
//     let formData=form.serialize();
//     $.ajax({
//     	'url':window.location.href,
//     	'type':form.attr('method'),
//     	'data':formData,
//     	'callback':function(resp){
//     		alert(resp);
//     	},
//     	'success':function(resp){
//     		window.location.reload();
//     	},
//     	'async':true,
// });//Ajax Url request sender
});//form on submit