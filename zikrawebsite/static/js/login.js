
function verify(a,b ){
   //alert("i love coding");
let students = [
   {name:"naira_mir",password:"701",link:"/index/contact"},
   {name:"taqwa_tamseel",password:"702",link:"/index/contact"},
   {name:"arbeena_riyaz",password:"703",link:"/index/contact"},
   {name:"aifham_arshid",password:"704",link:"/index/contact"},
   {name:"s_muneeb",password:"705",link:"/index/contact"},
   {name:"samma_syed",password:"706",link:"/index/contact"},
   {name:"ayat_altaf",password:"707",link:"/index/contact"},
   {name:"syed_ifra",password:"708",link:"/index/contact"},
   {name:"nadeema_mushtaq",password:"709",link:"/index/contact"},
   {name:"shoib_akhter",password:"710",link:"/index/contact"},
   {name:"snober",password:"711",link:"/index/contact"},
   {name:"zulqarnain",password:"712",link:"/index/contact"},
   {name:"afan_bilal",password:"713",link:"/index/contact"},
   {name:"mehak",password:"714",link:"/index/contact"},
   {name:"syed_ifham",password:"715",link:"/index/contact"},
   {name:"afnan_manzoor",password:"716",link:"/index/contact"},
   {name:"shahzada_faisal",password:"717",link:"/index/contact"},
   {name:"mohd_atif",password:"718",link:"/index/contact"},
   {name:"abrar_ul_haq",password:"719",link:"/index/contact"},
   {name:"mumin_maqbool",password:"720",link:"/index/contact"},
   {name:"shahid_gulzar",password:"721",link:"/index/contact"},
   {name:"owais_farooq",password:"722",link:"/index/contact"},

];
for(let i=0;i<students.length;i++){
   if(students[i].name===a && students[i].password===b){
     window.location.href=students[i].link;
     //alert(students[i].link);
   }
}
 //  alert("please provide a valid credentials");

}
  /*function myfunction(){
            alert("hhfgfdfffdfdf");
           var name=document.getElementById("n").value;
          // alert(name);
           var rollno=document.getElementById("r").value;
           alert(rollno);
          // window.location.href="{% url 'contact' %}" + "?r="+rollno;
           alert("done");
           //verify(name,rollno);
      }*/

      function myfunction() {
        
          var name =  document.getElementById("n").value;
            var rollno = document.getElementById("r").value;
            var url = 'contact?name='+name+'&rollno='+rollno;
            alert(url);
            
         var xhttp = new XMLHttpRequest();
         xhttp.onreadystatechange = function() {
           if (this.readyState == 4 && this.status == 200) {
           // document.getElementById("n").innerHTML = this.responseText;
            //document.getElementById("r").innerHTML = this.responseText;
            
           }
         };
        alert("ok");
        
         xhttp.open("GET", url, true);
         xhttp.send();
         
       }










                        
                 