jQuery(document).ready(function($) {
  $("img").hover(function() {
    var src = this.src;
    this.src = $(this).data("img");
    $(this).data("img", src);
  });
});