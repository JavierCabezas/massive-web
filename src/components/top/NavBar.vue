<template>
    <nav class="navbar navbar-default navbar-static-top yamm">
        <div class="container">
            <div class="navbar-header col-sm-12 col-md-6 col-lg-4">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-controls="navbar">
                    <span class="sr-only">MassiveWave</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#"><img src="../../img/mw-logo2.png" alt="logo"></a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><router-link to="/">Home</router-link></li>
                    <li><router-link to="/about">About</router-link></li>
                    <li><router-link to="/music-packs"> Music Packs </router-link></li>
                    <li><router-link to="/faq">FAQ</router-link></li>
                    <li><router-link to="/blog">Blog</router-link></li>
                </ul>
            </div>
        </div>
    </nav>
</template>