var tblClient;

function getData() {
    tblClient = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            }, //parameters
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "names"},
            {"data": "surnames"},
            {"data": "dni"},
            {"data": "birthday"},
            {"data": "address"},
            {"data": "gender.name"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#"  rel="delete"  class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';

                    return buttons;
                },
            },
        ],

        initComplete: function (settings, json) {

        },

    });
}


var modal_title;
$(function () {

    modal_title = $('.modal-title');


    getData()

    $('.btnAdd').on('click', function () {
        // console.log(modal_title)
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un cliente');
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalClient').modal('show');
    })

    $('#data tbody')
        .on('click', 'a[rel="edit"]', function () {

            modal_title.find('span').html('Edición de un cliente');
            modal_title.find('i').removeClass().addClass('fas fa-edit');
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="names"]').val(data.names);
            $('input[name="surnames"]').val(data.surnames);
            $('input[name="dni"]').val(data.dni);
            $('input[name="birthday"]').val(data.birthday);
            $('input[name="address"]').val(data.address);
            $('select[name="gender"]').val(data.gender.id);
            $('#myModalClient').modal('show');
        })
        .on('click', 'a[rel="delete"]', function () {

            modal_title.find('span').html('Edición de un cliente');
            modal_title.find('i').removeClass().addClass('fas fa-edit');
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submit_with_ajax(window.location.pathname, parameters, 'Confirmación', '¿Estás seguro de eliminar el siguiente registro?', function () {
                tblClient.ajax.reload();
            })
        })

    $('#myModalClient').on('shown.bs.modal', function () {
        // $('form')[0].reset();
    })

    $('form').on('submit', function (e) {
        e.preventDefault();
        // var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, parameters, 'Confirmación', '¿Estás seguro de realizar la siguiente acción?', function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload()
            // getData();
        })
    });
});