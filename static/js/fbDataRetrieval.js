
window.fbAsyncInit = function() {
    FB.init({
        appId      : '1603028726617777',
        cookie     : true,  // enable cookies to allow the server to access the session BASE.HTML
        xfbml      : true,  // parse social plugins on this page
        version    : 'v2.3' 
    });
    FB.Event.subscribe('auth.login', function (response) {
        window.location = "https://friendspeak.herokuapp.com";
    });

    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            statusChangeCallback(response);
        } 
        else {
            window.location = "https://friendspeak.herokuapp.com/logout/";
        } 
    });

    function statusChangeCallback(response) {
        // defines current login status of the person
        if (response.status === 'connected') {
            //address: The person's address
            //location: The person's current location as entered by them on their profile. This field is not related to check-ins
            //name,birthday,location,bio,address,locale,email,picture,taggable_friends,friends",
            FB.api(
                "/me?fields=location,taggable_friends,friends",
                function (response) {
                    if (response && !response.error) {
                        console.log('Successful login for: ' + response.name + ' Email: ' + response.email);
    
                        // Start: menu bar
                        var myFriendsArray = [];
                        var numberOfFriendsApp = response.friends.data.length;
                        var friendsApp = response.friends.data;
                        var profileFriendsApp = document.getElementById("profileFriendsApp");
                        var myFriends = "";

                        for (var i = 0; i < numberOfFriendsApp; i++) {
                            console.log(friendsApp[i]);
                            myFriends += "<li><a href='/profile/" + friendsApp[i].id + "/'><img class='menu-icon' src='https://graph.facebook.com/" + friendsApp[i].id + "/picture?width=200'>&nbsp;&nbsp;&nbsp;" + friendsApp[i].name + "</a></li>";
                            myFriendsArray.push(friendsApp[i].name);
                        }

                        var numberOfTaggableFriends = response.taggable_friends.data.length;
                        var data = response.taggable_friends.data;
                        //console.log('fbDataRetrieval, taggable_friends.data.length:'+numberOfTaggableFriends+', and taggable_friends.data:'+JSON.stringify(data));
                        var profileTaggableFriends = document.getElementById("profileTaggableFriends");
                        var taggableFriends = "";

                        for (var i = 0; i < numberOfTaggableFriends; i++) {
                            if (myFriendsArray.indexOf(data[i].name) > -1) {
                                //take out of taggable friends
                            } 
                            else {
                                taggableFriends += "<li><p id='sendInviteButton' style='margin:0;'><img class='menu-icon' src='" + data[i].picture.data.url + "'>&nbsp;&nbsp;&nbsp;" + data[i].name + "</p></li>";
                            }
                        }

                        $(document).on("click", "#sendInviteButton", function() {
                            FB.ui({
                                app_id: '1603028726617777',
                                method: 'send',
                                link: 'https://friendspeak.herokuapp.com',
                            });
                        });

                        profileFriendsApp.innerHTML = myFriends;
                        profileTaggableFriends.innerHTML = taggableFriends;
                        console.log(profileFriendsApp);
                        console.log(profileTaggableFriends);
                        // End: menu bar

                        if (response.location != 'undefined' && response.location != 'unknown') {
                            var location = response.location;
                        }
                        else {
                            var location = "unknown";
                        }
                        var profileLocation = document.getElementById("profileLocation");
                        profileLocation.innerHTML = location;

                    }
                    else {
                        console.log('error retrieving some shit:::'+JSON.stringify(response.error));
                    }
                }
            );
      
            function getUserLocation() {
                FB.api(
                    "/v2.0/me?fields=location",
                    function (response) {
                        if (response && !response.error) {
                            console.log('getUserLocation, location:'+JSON.stringify(response));
                        }
                        else {
                            console.log('error thrown in getUserLocation:'+response.error);
                        }
                    }
                );
            }
        }
        else if (response.status === 'not_authorized') {
            console.log('person is logged into FB but not app');
            // The person is logged into Facebook, but not your app.
            document.getElementById('status').innerHTML = 'Please log into FriendSpeak.';
        }
        else {
            // The person is not logged into Facebook; unsure if logged into app or not.
            console.log('fbDataRetrieval: person not logged into FB or app');
            //FB.login(function(response) {
                //taggable_friends,user_about_me,user_birthday,user_location
                //handle the response {"authResponse":null,"status":"unknown"} when exit out of dialog box
                //console.log('FB.login response handling: this was where strinfigy response happened');
            //}, {scope: 'public_profile,user_birthday,user_about_me,user_location,user_friends', 
            //return_scopes: true
            //});
            document.getElementById('status').innerHTML = 'Please log into Facebook.';
        }
    }
};
