console.log('Connected!')

const lists = document.querySelectorAll('.list');

let draggedItem = null;

for (let i = 0; i < window.list_items.length; i++) {
	const item = window.list_items[i];

	item.addEventListener('dragstart', function () {
		draggedItem = item;
		setTimeout(function() {
			item.style.display = 'none';
		}, 0);
	});

	item.addEventListener('dragend', function () {
		setTimeout(function () {
			draggedItem.style.display = 'block';
			draggedItem = null;
		}, 0);
	});

	for (let j = 0; j < lists.length; j++) {
		const list = lists[j];

		list.addEventListener('dragover', function (e) {
			e.preventDefault();
		});
		list.addEventListener('dragenter', function (e) {
			e.preventDefault();
			this.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
		});
		list.addEventListener('dragleave', function (e) {
			this.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
		});
		list.addEventListener('drop', function (e) {
			this.append(draggedItem);
			this.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
		});
	}
}