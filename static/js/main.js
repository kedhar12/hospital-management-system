// small JS helper for UI enhancements
document.addEventListener('DOMContentLoaded', function(){
  // enable bootstrap tooltips if any
  if (window.bootstrap) {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (el) { return new bootstrap.Tooltip(el) })
  }
});
