/**
 * Created by javier on 7/30/17.
 */
let login_status = {
    debug: true,
    state: {
        isLoggedIn: false
    },
    updateLogin: function(data) {
        if (this.debug) console.log('Logged in with', data);
        this.user_data = data;
        return {state: this.state, user_data: this.user_data};
    },
    //Resets all the local variables
    logOut: function () {
        if (this.debug) console.log('Logged out');
        this.state.token = '';
        this.state.isLoggedIn = false;
        this.user_data.name = null;
        this.user_data.surname = null;
        this.user_data.image_url = null;
        this.user_data.email = null;
        this.user_data.created_at = null;
        return this.state.isLoggedIn;
    }
};