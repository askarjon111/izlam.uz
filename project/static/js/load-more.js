const loadBtn = document.getElementById('load-more');
const spinner = document.getElementById('spinner');
const total = JSON.parse(document.getElementById('json-total').textContent);
const alert = document.getElementById('alert');

function loadmorePost() {
    var _current_item = $('.single_content').length
    const content_container = document.getElementById("contents");
    $.ajax({
        url: 'load-more',
        type: 'GET',
        data: {
            'loaded_item': _current_item
        },
        beforeSend: function () {
            loadBtn.classList.add('not-visible');
            spinner.classList.remove('not-visible');
        },
        success: function (response) {
            const data = response.object_list
            spinner.classList.add('not-visible')
            data.map(picture => {
                content_container.innerHTML += `<div class="single_content col-md-4 col-sm-6">
                                                        <div class="portfolio-item">
                                                            <div class="thumb">
                                                                <a href="https://izlam.uz/media/${picture.picture}" data-lightbox="image-1">
                                                                    <div class="hover-effect">
                                                                        <div class="hover-content">
                                                                            <h1>${picture.title}</em></h1>
                                                                            <p>{% if picture.painted_at %}{{ picture.painted_at }}{% endif %}</p>
                                                                        </div>
                                                                    </div>
                                                                </a>
                                                                <div class="image">
                                                                    <img src="https://izlam.uz/media/${picture.picture}">
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>`
            })
            if (_current_item == total) {
                alert.classList.remove('not-visible');
            } else {
                loadBtn.classList.remove('not-visible');
            }
        },
        error: function (err) {
            console.log(err);
        },
    });
}
loadBtn.addEventListener('click', () => {
    loadmorePost()
});