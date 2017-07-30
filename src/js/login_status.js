/**
 * Created by javier on 7/30/17.
 */
let login_status = {
    debug: true,
    state: {
        token: '',
        isLoggedIn: false
    },
    updateLogin: function(token) {
        if (this.debug) console.log('Logged in with', token);
        this.state.token = token;
        this.state.isLoggedIn = true;
        return (this.state);
    },
    logOut: function () {
        if (this.debug) console.log('Logged out');
        this.state.token = '';
        this.state.isLoggedIn = false;
        return (this.state);
    }
};