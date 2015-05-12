
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


function userInformation(userID){
      var userLocale = "en_US";
      var userDisplayName = "";
      var permissionDeclinedCount;
console.log('userInformation userID sent:'+userID);
      FB.api(
        '/me?fields=permissions,name,locale,birthday,picture,friends,taggable_friends,user_photos',
        function (response) {
          console.log('userInformation response:'+JSON.stringify(response));
          if (response && !response.error) {
               permissionDeclinedCount = 0;
               console.log('fbAuthLogin taggable_friends:'+JSON.stringify(response.taggable_friends));
               console.log('fbAuthLogin friends:'+JSON.stringify(response.friends));
               console.log('fbAuthLogin photos:'+JSON.stringify(response.user_photos));
               
                var permissionsArray = response.permissions.data;
                console.log('permissionsArray.count:'+permissionsArray.count);
                
                function inPermissions(arr) {
                  for(var i=0; i<arr.length; i++) {
                      if (arr[i]["status"] == "declined"){
                        permissionDeclinedCount++;
                        
                      }
                  }
                  if(permissionDeclinedCount >= 1){
                    console.log('permissions are not granted, logging out');
                    window.alert("Hi "+userDisplayName+", unfortunately we cannot log you in without gaining a little information about you so your friends know who they're posting/talking to. "+
                    "\n\nWe require your friend list (to display a list of friends that you can post to), email address (for user idenitification in our database), birthday (to calculate your age [your actual month/day is not displayed]), current city (so your friends know where you are), and personal description (as a template to start with that you can later change)"+
                    "\n\nWe will now log you out; when you log back in you will be prompted for permissions and we hope you understand why this information is necessary!");
                    
                    FB.logout(function(response){
                      console.log('user is logged out');
                    });
                
                    FB.login(function(response) {
                        console.log('rerequesting permissions');
                      }, {scope: 'user_birthday,user_about_me,user_location,user_friends',
                          auth_type: 'rerequest'
                     });
                    //ENSURE REREQUST POPUP WINDOW CLOSES (AND RELOAD PAGE/REDIRECT TO /HOME/)
                  }else{
                    console.log('all permissions granted');
                  }
                  if(response.status == 'connected'){
                    window.location = "https://friendspeak.herokuapp.com";
                  }
                }  
                
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
                  console.log('couldnt pass permissions, permissionCount:'+permissionCount);
              }
            }else{
              console.log('error: permissions retrieval::'+JSON.stringify(response));
            }
        }
      );

    }
