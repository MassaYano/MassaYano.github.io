<script>
(function($) {
$(document).ready(function(){
	var sideCategory = $('#sideCategory').get(0);
//console.log(sideCategory);
	$(sideCategory).find('.M_layer3').hide();
	$(sideCategory).find('.M_layer2').hide();

	$(sideCategory).find('.M_layer1 > li > a').each(function(){
		$(this).attr('href', 'javascript:void(0)');
		$(this).click(function(){
			var li = $(this).closest('li').get(0);
			var menu = $(li).find('ul.M_layer2').get(0);
			if ($(menu).is(':visible')) {
				$(menu).slideUp(300);
			} else {
				$(menu).slideDown(300);
			}
		});
	});
	$(sideCategory).find('.M_layer2 > li > a').each(function(){
	 	var li = $(this).closest('li').get(0);
		var menu = $(li).find('ul.M_layer3').get(0);
	 	if(typeof menu === 'undefined'){
//子が無い場合は aを残す
	 	}else{
			 $(this).attr('href', 'javascript:void(0)');
	 	 }
		$(this).click(function(){
			li = $(this).closest('li').get(0);
			menu = $(li).find('ul.M_layer3').get(0);
			if ($(menu).is(':visible')) {
				$(menu).slideUp(300);
			} else {
				$(menu).slideDown(300);
			}
		});
	});

	var current = $(sideCategory).find('.M_current').get(0);
	$(current).closest('.M_layer3').show();
	$(current).closest('.M_layer2').show();

});
})(jQuery);
