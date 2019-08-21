function loading(){
  // Add the loading wheel
    
  console.log('Got file !');
  var preloader = document.createElement( 'div' );
  $(preloader).attr("id","preloader");

  var loader = document.createElement( 'div' );
  $(loader).attr("id","loader-1");
  $(loader).attr("class","loader");
  // loader.innerHTML += "<br><br><p style='padding-left: -5px;'>Loading</p>"

  preloader.append(loader);
  $('body').append(preloader);

  // Blur the page
  el = document.getElementById('allContentPage');
  $(el).css("filter", "blur(15px)");
}