 // called with the results from from FB.getLoginStatus().
  function statusChangeCallback(response) {
    console.log('accessToken & status:'+JSON.stringify(response));
    
    var sendResponse = response;
    console.log('statusChangeCallback sendResponse:'+sendResponse);
     if (response.status === 'connected') {
     var userID = sendResponse.authResponse.userID;
      userInformation(userID);
            
  //console.log('end of userInformation function, permissionsDeclined:'+permissionCount);
    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      console.log('response.status==not_authorized: logged into fb but not app; logging out of fb now');
      document.getElementById('status').innerHTML = 'Please log in to facebook again ';
    } else {
      console.log('user is not logged into facebook');
      // person not logged into Facebook; unsure if they're logged into app or not.
      // document.getElementById('status').innerHTML = 'Please log into Facebook.';
      
      
    }
  }
  
  
  
  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }

window.fbAsyncInit = function() {
  FB.init({
    appId      : '1565760477011269',
    cookie     : true,  
    xfbml      : true,  
    version    : 'v2.3' 
  });
  FB.Event.subscribe('auth.login', function (response) {
      window.location = "https://friendspeak.herokuapp.com";
 });

  FB.getLoginStatus(function(response) {
          statusChangeCallback(response);
  });
  
};
  //load the SDK asynchronously
   (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.3&appId=1565760477011269";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk')); 

function newLoginDialog(){
    FB.login(function(response) {
    console.log('INSIDE newLoginDialog; rerequesting permissions');
    },
    {
      scope: 'user_birthday,user_about_me,user_location,user_friends',
      auth_type: 'rerequest'
      return_scopes: true
   });
}
function userInformation(userID){
      var userLocale = "en_US";
      var userDisplayName = "";
      var permissionDeclinedCount;
      console.log('userInformation userID sent:'+userID+' making fb.api call.');

      FB.api(
        '/me?fields=permissions,name,locale,birthday,picture',
        function (response) {
          console.log('userInformation response in fb.api call:'+JSON.stringify(response));
          if (response && !response.error) {
               permissionDeclinedCount = 0;
                var permissionsArray = response.permissions.data;
                console.log('full response'+JSON.stringify(response));
                console.log('response.permissions: '+JSON.stringify(response.permissions));
                console.log('permissionsArray.count:'+permissionsArray.count);
                

 //               console.log('right before inPermissions (1)');
                function inPermissions(arr) {
//                  console.log('inside inPermissions (3)')
                  for(var i=0; i<arr.length; i++) {
                      if (arr[i]["status"] == "declined"){
                        permissionDeclinedCount++; 
                      }
                      console.log('inPermissions(arr) for loop');
                  }
                  if(permissionDeclinedCount >= 1){
                    console.log('permissionCount >= 1, they denied:'+permissionDeclinedCount+' permissions');
                    window.alert("Hi "+userDisplayName+", unfortunately we cannot log you in without gaining a little information about you so your friends know who their posting/talking to. "+
                    "\n\nWe require your friend list (to display a list of friends that you can post to), email address (for user idenitification in our database), birthday (to calculate your age [actual month/day is not displayed]), current city (so your friends know where you are), and personal description (as a template to start with that you can later change)"+
                    "\n\nWe will now log you out; when you log back in you will be prompted for permissions and we hope you understand why this information is necessary!");
                    
                    console.log('after alert window; permissions are not granted, SKIPPING LOGOUT, running newLoginDialog');
                    
                    newLoginDialog();
                    //FB.logout(function(response){
                      //console.log('user is logged out');
                    //});
                
                    console.log('JUST RAN newLoginDialog::::::DID NOT stopped loggout, TRYING TO CALL FOR REREQUEST LOG BACK IN ');
                    
                    
                      console.log('after fb.login within fbAuthLogin.js to see if grantedScopes of authresponse works:'+authResponse.grantedScopes);
                      
                     window.alert('login rerequest has been sent; hopefully this breaks back to rerequest permissions on submit....');
                    //ENSURE REREQUST POPUP WINDOW CLOSES (AND RELOAD PAGE/REDIRECT TO /HOME/)
                  }else{
                    console.log('all permissions granted');
                  }
                  if(response.status == 'connected'){
                    window.location = "https://friendspeak.herokuapp.com";
                  }
                }  
//                console.log('calling inPermissions now (2)');
                inPermissions(permissionsArray);
                
                console.log('declined permissions::'+permissionDeclinedCount);
              if(permissionDeclinedCount == 0 ){
                var profName = response.name;
                var profLocale = response.locale;
                var profAge;
                var profPicture = "https://graph.facebook.com/" + userID + "/picture?width=200";
                
                function agefinding()
                     {
                        var birthDay = response.birthday;
                        var DOB = new Date(birthDay);
                        var today = new Date();
                        var ageCalc = today.getTime() - DOB.getTime();
                        ageCalc = Math.floor(ageCalc / (1000 * 60 * 60 * 24 * 365.25));
                        return ageCalc;
                    }                  
                  if(response.birthday != 'undefined'){
                    profAge = agefinding();
                    console.log('age:'+profAge);
                  }else{
                    profAge = 'null';
                    console.log('cant find age');
                  }                
                
                  document.getElementById("profilePicture").value = profPicture;
                  document.getElementById("profileName").value = profName;
                  document.getElementById("profileLocale").value = profLocale;
                  document.getElementById("profileAge").value = profAge;       
                  document.getElementById("profileUserID").value = userID;         //userID
                  document.getElementById("password").value = "12345";    //super secret password key
                  console.log('found username and password elements');
                  document.getElementById('loginForm').submit();
                  console.log('login form just submitted');
              }else{
                  console.log('couldnt pass permissions, permissionDeclinedCount:'+permissionDeclinedCount);
              }
            }else{
              console.log('error: permissions retrieval::'+JSON.stringify(response));
            }
        }
      );

    }
