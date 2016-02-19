/*!
 * Start Bootstrap - Creative Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

(function($) {
    "use strict"; // Start of use strict

    var isFirefox = (navigator.userAgent.toLowerCase().indexOf('firefox') > -1);
    var isMobile = (typeof window.orientation !== "undefined") ||
                   (navigator.userAgent.indexOf('IEMobile') !== -1);

    if(isFirefox && !isMobile) {
        $('a[href^="tel:"]').click(function() { return false; });
    }

})(jQuery); // End of use strict
