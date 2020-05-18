<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>IAO | Weather | Forecast</title>
  <meta content="" name="descriptison">
  <meta content="" name="keywords">
  <!--<meta http-equiv="refresh" content="10" /> -->

  <!-- Favicons -->
  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/icofont/icofont.min.css" rel="stylesheet">
  <link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="assets/vendor/venobox/venobox.css" rel="stylesheet">
  <link href="assets/vendor/owl.carousel/assets/owl.carousel.min.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="assets/css/style.css" rel="stylesheet">

<style>
	.blink-text{
		color: #000;
		font-weight: bold;
		font-size: 1.1rem;
		animation: blinkingText 2s infinite;
	}
	@keyframes blinkingText{
		0%		{ color: #10c018;}
		25%		{ color: #1056c0;}
		50%		{ color: #ef0a1a;}
		75%		{ color: #254878;}
		100%	{ color: #04a1d5;}
	}
</style>

</head>

<body>

  <!-- ======= Mobile nav toggle button ======= -->
  <button type="button" class="mobile-nav-toggle d-xl-none"><i class="icofont-navigation-menu"></i></button>

  <!-- ======= Header ======= -->
  <header id="header">
    <div class="d-flex flex-column">

      <div class="profile">
        <img src="assets/img/profile-img.gif" class="img-fluid ">
        <h1 class="text-light"><a href="index.html">IAO | Weather</a></h1>
        
      </div>

      <nav class="nav-menu">
        <ul>
		 <li class="active"><a href="../index.html"><i class="bx bx-home"></i> <span>Home</span></a></li>
          <li><a href="#about"><i class="bx bx-star"></i> <span>All Sky Camera</span></a></li>
          <li><a href="#resume"><i class="bx bxs-planet"></i> <span>Object Visibility</span></a></li>
          <li><a href="#portfolio"><i class="bx bx-cloud"></i> Weather Forecast</a></li>
         

        </ul>
      </nav><!-- .nav-menu -->
      <button type="button" class="mobile-nav-toggle d-xl-none"><i class="icofont-navigation-menu"></i></button>

    </div>
  </header><!-- End Header -->


  <main id="main">

    <!-- ======= About Section ======= -->
    <section id="about" class="about">
      <div class="container">

        <div class="section-title">
          <h2>IAO AllSky Camera</h2>

		</div>

       		
		<div class="row">
          <div class="col-lg-6" data-aos="fade-right">
 <a href="allskycamera/latest.png" target="_blank">
		 
            <img src="allskycamera/latest.png" class="img-fluid"  alt="Live Sky" width="1000" height="500"> </a>
          </div>
          <div class="col-lg-6 pt-3 pt-lg-0 content" data-aos="fade-left">
            <h3> About the System</h3>

		
		
	
        
           
			<p>
			  
The IAO all-sky camera is a wide-angle camera system that takes images of the sky every 30 seconds,
day and night. It is based on an Adirondack Video Astronomy StellaCam II video camera and utilizes an auto-iris
fish-eye lens to allow safe operation under all lighting conditions, even direct sunlight. This combined with the
anti-blooming characteristics of the StellaCam’s detector allows useful images to be obtained during sunny days
as well as brightly moonlit nights. Under dark skies the system can detect stars as faint as 6th magnitude.
<br><b>
 The system has been automated to change its parameters for different lighting conditions.</b>
			</p>
                 <b><p class="font-italic"><a href="allskycamera" target="_blank">Click here to view archive images and movies</a> </p>

           </b>
<br>
            
			<div class="blink-text"> <p>We are currently having problem with image quality due to a minor hardware issue. Resolving the problem soon.</p></div>

          
             
             
            
           
          </div>
        </div>

		
		
		
          

      </div>
    </section><!-- End About Section -->

 <section id="resume" class="resume section-bg">
      <div class="container">

        <div class="section-title">
          <h2>Object Visibility</h2>

<div class="row">
          <div class="col-lg-6" data-aos="fade-right">
            <form action="forms/contact.php" method="post" role="form" class="php-email-form">
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="name">RA</label>
                  <input type="text" name="name" class="form-control" id="RA" data-msg="Enter RA (in J2000) " />
                  <div class="validate"></div>
                </div>
                <div class="form-group col-md-6">
                  <label for="name">DEC</label>
                  <input type="text" class="form-control" id="DEC"  data-msg="Enter DEC (in J2000) " />
                  <div class="validate"></div>
                </div>
              </div>
        
              <div class="text-center"><button type="submit">Submit</button></div>
            </form>

          </div>
          <div class="col-lg-6 pt-3 pt-lg-0 content" data-aos="fade-left">
             
           
			<p>
			  

<br><p>
This program shows the observability of an object with plot of altitude against time for tonight. <br>         
Formats :   hh mm ss ±dd mm ss  OR  ddd.ddd dd.ddd
 
</p>

			</p>

              

             
             
            
           
          </div>
        </div>


<br>
<h3> Some Important conditions for tonight </h3>
<div class="row ">

<div class="col-lg-12 d-flex justify-content-center">
 <a href="allskycamera/tonight.png" target="_blank">
		<img id="imgFore" class="img-fluid" src="allskycamera/tonight.png" width="1000" height="500"> </a>
        
</div>

</div></div>

        <div class="row">
          <div class="col-lg-6" data-aos="fade-up">
           

            <div class="resume-item pb-0">
             
 <a href="allskycamera/moon_motion.png" target="_blank">
		<img id="imgFore" class="img-fluid" src="allskycamera/moon_motion.png" width="1000" height="500"> </a>
     
            
            </div>

         
          </div>
          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
            


            <div class="resume-item">
              <a href="allskycamera/planets_motion.png" target="_blank">
		<img id="imgFore" class="img-fluid" src="allskycamera/planets_motion.png" width="1000" height="500"> </a>
            </div>
          </div>
        </div>

      </div>
    </section><!-- End Resume Section -->


    <!-- ======= Portfolio Section ======= -->
    <section id="portfolio" class="portfolio ">
      <div class="container">

        <div class="section-title">
		 <h2>Weather Forecast</h2>
		 
		 <p>Real-time update from: 7timer,  yr forecast, MeteoBlue, Accuweather and Forecast7.</p>
		 <br>

<div class="row" data-aos="fade-up">


 <div class="col-lg-12 d-flex justify-content-center">
  <a href="http://www.7timer.info/bin/astro.php?lon=78.965&lat=32.779&lang=en&ac=0&unit=metric&tzshift=0" target="_blank">
		<img id="imgFore" class="img-fluid" src=http://www.7timer.info/bin/astro.php?lon=78.965&lat=32.779&lang=en&ac=0&unit=metric&tzshift=0 width="1000" height="500"> </a>

</div>
  </div>

<br>

<div class="row" data-aos="fade-up">
<div class="col-lg-12 d-flex justify-content-center">
<a href="https://www.yr.no/en/details/graph/2-1270426/India/Jammu%20and%20Kashmir/Lad%C4%81kh/Hanle" target="_blank">
		<img id="imgFore" class="img-fluid" src=https://www.yr.no/place/India/Jammu_and_Kashmir/Hanle/meteogram.png width="1000" height="500"> </a>

</div>
</div>

         
      
		
		 
	

                    
			
		
    	   </div>

        <div class="row" data-aos="fade-up">
          <div class="col-lg-12 d-flex justify-content-center">
            <ul id="portfolio-flters">
              <li data-filter="*" class="filter-active">All</li>
              <li data-filter=".filter-app">IMD</li>
              <li data-filter=".filter-web">7timer</li>
            </ul>
          </div>
        </div>

        <div class="row portfolio-container" data-aos="fade-up" data-aos-delay="100">

          <div class="col-lg-4 col-md-6 portfolio-item filter-app">
            <div class="portfolio-wrap">
              <img src="http://www.7timer.info/bin/civil.php?lon=78.965&lat=32.779&lang=en&ac=0&unit=metric&tzshift=0" class="img-fluid"  alt="7timer" width="1000" height="500">
			
              <div class="portfolio-links">
                <a href="http://www.7timer.info/bin/civil.php?lon=78.965&lat=32.779&lang=en&ac=0&unit=metric&tzshift=0" data-gall="portfolioGallery" class="venobox" title="App 1"><i class="bx bx-plus"></i></a>
                
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 portfolio-item filter-web">
            <div class="portfolio-wrap">
              <img src="http://www.7timer.info/bin/meteo.php?lon=78.965&lat=32.779&lang=en&ac=0&unit=metric&tzshift=0" class="img-fluid"  alt="7timer" width="1000" height="500">
			
			
              <div class="portfolio-links">
                <a href="http://www.7timer.info/bin/meteo.php?lon=78.965&lat=32.779&lang=en&ac=0&unit=metric&tzshift=0" data-gall="portfolioGallery" class="venobox" title="App 2"><i class="bx bx-plus"></i></a>
              
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-6 portfolio-item filter-app">
            <div class="portfolio-wrap">
			<img src="https://mausam.imd.gov.in/Satellite/3Dasiasec_ir1.jpg" class="img-fluid"  alt="7timer" width="1000" height="500">
             
              <div class="portfolio-links">
                <a href="https://mausam.imd.gov.in/Satellite/3Dasiasec_ir1.jpg" data-gall="portfolioGallery" class="venobox" title="Web 2"><i class="bx bx-plus"></i></a>

              </div>
            </div>
          </div>


        </div>

      </div>
	  
	  
    </section><!-- End Portfolio Section -->

   


    <!-- ======= Contact Section ======= -->
    <section id="contact" class="contact section-bg">
      <div class="container">

        <div class="section-title">
         
		
		</div>

        <div class="row" data-aos="fade-in">

          <div class="col-lg-6 d-flex align-items-stretch">
            <div class="info">
			
				  <div id="Container"
 style="padding-bottom:136.25%; position:relative; display:block; width: 100%">
 <iframe id="ViostreamIframe" 
  width="100%" height="100%" 
  src="https://www.meteoblue.com/en/weather/widget/three/hanle_india_1270426?geoloc=fixed&nocurrent=0&noforecast=0&days=4&tempunit=CELSIUS&windunit=KILOMETER_PER_HOUR&layout=image"
  frameborder="0" allowfullscreen=""
  style="position:absolute; top:0; left: 0"></iframe>
</div>       
             
			</div>

          </div>

          <div class="col-lg-6 mt-5 mt-lg-0 d-flex align-items-stretch">
		  <div class="info">
	           <div id="Container"
 style="padding-bottom:136.25%; position:relative; display:block; width: 100%">
 <iframe id="ViostreamIframe" 
  width="100%" height="100%" 
  src="https://www.meteoblue.com/en/weather/widget/seeing/hanle_india_1270426?geoloc=fixed&noground=0"
  frameborder="0" allowfullscreen=""
  style="position:absolute; top:0; left: 0"></iframe>
</div>     
          </div>
          </div>

        </div>

      </div>
    </section><!-- End Contact Section -->

  </main><!-- End #main -->

  <!-- ======= Footer ======= -->
  <footer id="footer">
    <div class="container">
      <div class="copyright">
        &copy; <strong><span>Indian Astronomical Observatory 2020.</span></strong>
      </div>
      <div class="credits">
 
        The forecast datas are loaded in real-time from APIs provided by best weather channels in public domain. <br>  Credits: Weather forecast from Yr provided by Meteorological Institute 
				and NR,   7timer, Accuweather, MeteoBlue , Forecast7 and IMD, India.
      </div>
    </div>
  </footer><!-- End  Footer -->

  <a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

  <!-- Vendor JS Files -->
  <script src="assets/vendor/jquery/jquery.min.js"></script>
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/jquery.easing/jquery.easing.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>
  <script src="assets/vendor/waypoints/jquery.waypoints.min.js"></script>
  <script src="assets/vendor/counterup/counterup.min.js"></script>
  <script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="assets/vendor/venobox/venobox.min.js"></script>
  <script src="assets/vendor/owl.carousel/owl.carousel.min.js"></script>
  <script src="assets/vendor/typed.js/typed.min.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>

  <!-- Template Main JS File -->
  <script src="assets/js/main.js"></script>

</body>

</html>
