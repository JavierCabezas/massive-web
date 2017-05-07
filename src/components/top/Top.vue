<template>
    <header class="header">
        <!--top bar-->
        <div class="top-bar">
            <div class="container">
                <div class="row">
                    <div class="col-sm-12 text-right">
                        <ul class="list-inline">
                            <li class="hidden-xs"><a href="#/register"><i class="fa fa-user"></i> Account </a></li>
                            <li><a href="#/login"><i class="pe-7s-lock"></i> Login </a></li>
                            <li class="lang-dropdown">
                                <a> English </a>
                                <div class="lang-drop-menu">
                                    <a><img src="../../img/flag_en.png"> English </a>
                                    <a><img src="../../img/flag_es.png"> Spanish </a>
                                </div>
                            </li>
                            <li><a href="javascript:void(0)" class="search-toggle"><i class="fa fa-search"></i></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <!--top bar end-->


        <!--main navigation start-->
        <!-- Static navbar -->
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
                        <li class="active"><a href="#/home"> Home </a></li>
                        <li><a href="#/about"> About </a></li>
                        <li><a href="#/musicpacks"> Music packs </a></li>
                        <li><a href="#/faq"> FAQ </a></li>
                        <li><a href="#/blog"> Blog </a></li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
</template>