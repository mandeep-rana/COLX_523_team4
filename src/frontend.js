
function clearFields() {
document.getElementById("form").reset();
}   

function update_value() {
    document.getElementById("courses").value = "courses";
    update_page()  

}  

function check_blank() {
	var textbox = document.getElementById("textbox").value;
    

    if (!textbox.match(/\S/)) 
	{ 
		alert("Please input search text!");
	}                                                    
	else if (textbox != "")
    {
        var spclChars = "!@#$%^&*()"; // specify special characters
           
        for (var i = 0; i < textbox.length; i++)
        {
            if (spclChars.indexOf(textbox.charAt(i)) != -1)
                {
                    alert ("Special characters are not allowed.");
                    document.getElementById("textbox").value = "";
                    return false;
                }
            else 
                {
                   update_page()
                } 
                
        }   
        
    }

}  

function check_blank1() {
	var textbox = document.getElementById("textbox1").value;
    if (!textbox.match(/\S/)) 
	{ 
		alert("Please input search text!");
	}                                                    
    else if (textbox != "")
        {
            var spclChars = "!@#$%^&*()"; // specify special characters

            for (var i = 0; i < textbox.length; i++)
            {
                if (spclChars.indexOf(textbox.charAt(i)) != -1)
                    {
                        alert ("Special characters are not allowed.");
                        document.getElementById("textbox").value = "";
                        return false;
                    }
                else 
                    {
                       update_page()
                    } 

            }   

        }

}   


function check_blank2() {
	var textbox = document.getElementById("textbox2").value;
    if (!textbox.match(/\S/)) 
	{ 
		alert("Please input search text!");
	}                                                    
    else if (textbox != "")
        {
            var spclChars = "!@#$%^&*()"; // specify special characters

            for (var i = 0; i < textbox.length; i++)
            {
                if (spclChars.indexOf(textbox.charAt(i)) != -1)
                    {
                        alert ("Special characters are not allowed.");
                        document.getElementById("textbox").value = "";
                        return false;
                    }
                else 
                    {
                       update_page()
                    } 

            }   

        }

}   

function insert_result(response) {
	 var maintext = document.getElementById("maintext");
	 maintext.innerHTML = response;
}


function update_page() {
	var form = document.getElementById("form");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest( )
	xmlHttpRqst.onload = function(e) {insert_result(xmlHttpRqst.response);} 
	xmlHttpRqst.open( "GET", "/pos/?" + queryString);
	xmlHttpRqst.send();
    document.getElementById("courses").value = "";
	
}



