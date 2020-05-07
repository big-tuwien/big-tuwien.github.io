/* ---------------------------------------------------------------------------
 * Filter Courses.
 * --------------------------------------------------------------------------- */

// Course container.
let $grid_courses = $('#container-courses');

let $semester_filter = $('.courses-filter');

let semesterValue = $semester_filter.children("option:selected").val();

function filter(semester) {
  const selector = '.semester-' + semester;
  const $semesters = $grid_courses.find('.semester');
  $semesters.filter(selector).show();
  $semesters.not(selector).hide();
}

// filter items on button click
$semester_filter.on('change', function () {
  semesterValue = $(this).children("option:selected").val();
  // Apply filter
  filter(semesterValue);
});

// Filter courses according to hash in URL.
function filter_courses() {
  let urlHash = window.location.hash.replace('#', '');

  // Check if semester hash is valid
  if (urlHash !== '' && urlHash.match(/\d{4}[SW]/)) {
    semesterValue = urlHash;
  }

  // Apply filter
  filter(semesterValue);

  // Set selected option.
  $semester_filter.val(semesterValue);
}

$(window).on('load', function () {
  // Enable course filter for course index page.
  if ($('.courses-widget')) {
    filter_courses();
    // Useful for changing hash manually (e.g. in development):
    window.addEventListener('hashchange', filter_courses, false);
  }
});
