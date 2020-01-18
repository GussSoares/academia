var TableDatatablesAjax = function () {

    var grid;

    var initPickers = function () {
        // init date pickers
        // $('.date-picker').datepicker({
        //     format:'dd/mm/yyyy',
        //     todayHighlight: true,
        //     autoclose: true,
        //     daysOfWeekHighlighted: "0,6",
        //     language: "pt-BR"
        // });
    };

    var initSelects = function () {
        // ComponentsSelect2.init();
    };

    var handleExercicios = function (tipo) {

        grid = new Datatable();

        grid.init({
            src: $("#datatable_ajax"),
            onSuccess: function (grid, response) {
                // grid:        grid object
                // response:    json object of server side ajax response
                // execute some code after table records loaded
            },
            onError: function (grid) {
                // execute some code on network or other general error
            },
            onDataLoad: function(grid) {
                // execute some code on ajax data load
                // $("#datatable_ajax > tbody > tr > td:last-child").addClass("clearfix");
                // $("#datatable_ajax > tbody > tr > td:last-child > .btn-group > .dropdown-menu").css("overflow", 'visible' );
                // $("#datatable_ajax > tbody > tr > td:last-child > .btn-group > .dropdown-menu").css("position", 'relative' );
                // $("#datatable_ajax > tbody > tr > td:last-child > .btn-group > .dropdown-menu").css("z-index", 99999 );
            },
            // loadingMessage: 'Carregando...',
            dataTable: { // here you can define a typical datatable settings from http://datatables.net/usage/options

                // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
                // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/scripts/datatable.js).
                // So when dropdowns used the scrollable div should be removed.

                //"dom": "<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'<'table-group-actions pull-right'>>r><'table-responsive't><'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>", // datatable layout
                "dom": "<'row'<'col-md-12 col-sm-12'<'table-group-actions pull-right'>>r><'row'<'col-md-8 col-sm-12'pli>r><'table-responsive't><'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>",
                // "dom": "<'row'<'col-md-12 col-sm-12'<'table-group-actions pull-right'>>r><'row'<'col-md-8 col-sm-12'pli>r><'table-responsive' t><'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>",
                "bStateSave": true, // save datatable state(pagination, sort, etc) in cookie.
                "language": { // language settings
                        // metronic spesific
                        "metronicGroupActions": "_TOTAL_ registros selecionados:  ",
                        "metronicAjaxRequestGeneralError": "Não foi possível concluir o pedido. Por favor, verifique sua conexão à internet.",

                        // data tables spesific
                        "lengthMenu": "<span class='seperator'>&ensp;&ensp;|&ensp;&ensp;</span>Ver _MENU_ registros",
                        "info": "<span class='seperator'></span>de _TOTAL_.",
                        "infoEmpty": "Nenhum registro encontrado.",
                        "emptyTable": "Sem dados disponíveis na tabela.",
                        "zeroRecords": "Nenhum registro correspondente foi encontrado.",
                        "paginate": {
                            "previous": "Ant.",
                            "next": "Prox.",
                            "last": "Último",
                            "first": "Primeiro",
                            "page": "Página",
                            "pageOf": "de"
                        }
                    },
                "lengthMenu": [
                    // [10, 20, 50, 100],
                    // [10, 20, 50, 100] // change per page values here
                    // [10, 20, 50, 100, 150, -1],
                    // [10, 20, 50, 100, 150, "Todos"] // change per page values here
                    [10, 20, 50, 100, 150, 300],
                    [10, 20, 50, 100, 150, 300] // change per page values here
                ],
                "pageLength": 10, // default record count per page
                "processing": true,
                "serverSide": true,
                "ajax": {
                    "type": "GET", // request type
                    "processing": false,
                    "url": "/exercicio/api/list-exercicio-ajax/",
                    "data": function(data) { // add request parameters before submit
                        grid.setAjaxParam('tipo', tipo);
                        var ajaxParams = grid.getAjaxParams();
                        $.each(ajaxParams, function(key, value) {
                            data[key] = value;
                        });
                    },
                },
                "columns": [
                    { "data": "id", "defaultContent": "<i>-</i>" },
                    { "data": "nome", "defaultContent": "<i>-</i>" },
                    { "data": "descricao", "defaultContent": "<i>-</i>" },
                    { "data": "acoes", "defaultContent": "<i>-</i>" },
                ],
                "columnDefs": [ // define columns sorting options(by default all columns are sortable extept the first checkbox column)
                    {
                        'orderable': false,
                        'targets': [3]
                    },
                    {
                        'render': function ( data, type, row ) {

                            return data;
                        },
                        'targets': 1
                    },
                    {
                        'render': function (data, type, row) {
                            var words = data.split(' ');
                            var show_words = '';
                            if (words.length > 6) {
                                for (var i = 0; i < 6; i++) {
                                    show_words += (words[i] + ' ');
                                }
                                show_words += '...';
                                return show_words;
                            }
                            return data
                        },
                        'targets': 2
                    },
                    {
                        'render': function (data, type, row) {
                            // return `<a id="editar" class="PageLink" title="Editar"><i class="fa fa-edit"></i></a>`+
                            return `<a href="/exercicio/api/edit-exercicio-modal/${row.id}" data-target="#ajax" data-toggle="modal"><i class="fa fa-edit"></i></a>`
                        },
                        'targets': 3
                    }
                ],
                "order": [
                    [0, "asc"]
                ],// set first column as a default sort by asc
                buttons: [
                    { extend: 'print', className: 'btn default' },
                    { extend: 'copy', className: 'btn default' },
                    { extend: 'pdf', className: 'btn default' },
                    { extend: 'excel', className: 'btn default' },
                    { extend: 'csv', className: 'btn default' },
                    {
                        text: 'Reload',
                        className: 'btn default',
                        action: function ( e, dt, node, config ) {
                            dt.ajax.reload();
                            alert('Datatable reloaded!');
                        }
                    }
                ],
            }
        });

        // handle group actionsubmit button click
        grid.getTableWrapper().on('click', '.table-group-action-submit', function (e) {
            e.preventDefault();
            setAlertas();
            grid.clearAjaxParams();
            setParamsBusca();
            grid.getDataTable().ajax.reload();
        });

        // handle datatable custom tools
        $('#datatable_ajax_tools > li > a.tool-action').on('click', function() {
            var action = $(this).attr('data-action');
            grid.getDataTable().button(action).trigger();
        });

        // handle edit option in actions
        $('table').on('click', '.PageLink', function(){
            // grid.getDataTable().ajax.reload();

            let aux_this = $(this);
            let rowData = $('table').DataTable().row($(this).closest('tr')).data();
            let colNome = $(this).parent().siblings()[1];
            let colDescricao = $(this).parent().siblings()[2];
            // cancelar_without_reload(rowData, colNome, colDescricao, aux_this);
            // editar(rowData, colNome, colDescricao, aux_this);
            $(colNome).html(`<input id="temp_nome" class="form-control" value="${rowData.nome}" type="text" />`);
            $(colDescricao).html(`<input id="temp_desc" class="form-control" value="${rowData.descricao}" type="text" />`);
            $(aux_this).html(`<a id="salvar" class="PageLink" title="Salvar"><i style="color:green" class="fa fa-check"></i></a>` +
                                `<a id="cancelar" class="PageLink" title="Cancelar"><i style="color:red" class="fa fa-times"></i></a>`);
            // preciso mudar os campos de cada coluna da linha por um input;
            $('#salvar').click(function () {
                salvar(rowData);
            });

            $('#cancelar').click(function () {
                cancelar(rowData, colNome, colDescricao, aux_this);
            });
        });

        // function editar_modal(rowData, colNome, colDescricao, aux_this) {
        //
        // }

        function salvar(rowData) {
            $.ajax({
                method: 'GET',
                url: '/exercicio/api/edit-exercicio-ajax/',
                header: {'csrfmiddlewaretoken': csrf_token},
                data: {
                    'csrfmiddlewaretoken': csrf_token,
                    'id': rowData.id,
                    'nome': $('#temp_nome').val(),
                    'descricao': $('#temp_desc').val()
                },
                success: function (data) {
                    grid.getDataTable().ajax.reload();
                    toastr.success(data['msg'], {timeOut: 5000});
                },
                error: function (data) {
                    toastr.warning(data['msg'], {timeOut: 5000});
                }
            })
        }

        function cancelar(rowData, colNome, colDescricao, aux_this) {
            $(colNome).html(rowData.nome);
            $(colDescricao).html(rowData.descricao);
            $(aux_this).html(`<a id="editar" class="PageLink" title="Editar"><i class="fa fa-edit"></i></a>`);
            grid.getDataTable().ajax.reload();
        }

        function cancelar_without_reload(rowData, colNome, colDescricao, aux_this) {
            $(colNome).html(rowData.nome);
            $(colDescricao).html(rowData.descricao);
            $(aux_this).html(`<a id="editar" class="PageLink" title="Editar"><i class="fa fa-edit"></i></a>`);
            // grid.getDataTable().ajax.reload();
        }

        function setParamsBusca() {
            // var descricao = $("#id_descricao", grid.getTableWrapper()).val();
            // if (descricao){
            //     grid.setAjaxParam("descricao", descricao);
            // }
            // var cliente = $("#id_cliente", grid.getTableWrapper()).val();
            // if (cliente){
            //     grid.setAjaxParam("cliente", cliente);
            // }
            // var periodo = $("#id_periodo", grid.getTableWrapper()).val();
            // if (periodo){
            //     grid.setAjaxParam("periodo", periodo);
            // }
            // var data_ini = $("#id_data_inicio", grid.getTableWrapper()).val();
            // if (data_ini){
            //     grid.setAjaxParam("data_ini", data_ini);
            // }
            // var data_fim = $("#id_data_fim", grid.getTableWrapper()).val();
            // if (data_fim){
            //     grid.setAjaxParam("data_fim", data_fim);
            // }
            // var status = $("#id_status", grid.getTableWrapper()).val();
            // status = status || '0';
            // if (status){
            //     grid.setAjaxParam("status", status);
            // }
            // var banco = $("#id_banco", grid.getTableWrapper()).val();
            // if (banco){
            //     grid.setAjaxParam("banco", banco);
            // }
            // var forma_pagamento = $("#id_forma_pagamento", grid.getTableWrapper()).val();
            // if (forma_pagamento){
            //     grid.setAjaxParam("forma_pagamento", forma_pagamento);
            // }
            // var categoria = $("#id_categoria", grid.getTableWrapper()).val();
            // if (categoria){
            //     grid.setAjaxParam("categoria", categoria);
            // }
            // var centro_custos = $("#id_centro_custos", grid.getTableWrapper()).val();
            // if (centro_custos){
            //     grid.setAjaxParam("centro_custos", centro_custos);
            // }
        }

        function setAlertas() {
            $('.custom-alerts').remove();
            var periodo = $("#id_periodo", grid.getTableWrapper()).val();
            var data_ini = $("#id_data_inicio", grid.getTableWrapper()).val();
            var data_fim = $("#id_data_fim", grid.getTableWrapper()).val();
            if (periodo && data_ini && data_fim) {
                return 0
            } else if (periodo || data_ini || data_fim){
                App.alert({
                    type: 'danger',
                    icon: 'warning',
                    message: 'Para buscar um período, preencha os três campos: Período, Data início e Data Fim.',
                    container: grid.getTableWrapper(),
                    place: 'prepend'
                });
                return 1
            }
        }

    };

    var handleDemo1 = function () {

        var grid = new Datatable();

        grid.init({
            src: $("#datatable_ajax"),
            onSuccess: function (grid, response) {
                // grid:        grid object
                // response:    json object of server side ajax response
                // execute some code after table records loaded
            },
            onError: function (grid) {
                // execute some code on network or other general error
            },
            onDataLoad: function(grid) {
                // execute some code on ajax data load
            },
            loadingMessage: 'Loading...',
            dataTable: { // here you can define a typical datatable settings from http://datatables.net/usage/options

                // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
                // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/scripts/datatable.js).
                // So when dropdowns used the scrollable div should be removed.
                //"dom": "<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'<'table-group-actions pull-right'>>r>t<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>",

                "bStateSave": true, // save datatable state(pagination, sort, etc) in cookie.

                "lengthMenu": [
                    [10, 20, 50, 100, 150, -1],
                    [10, 20, 50, 100, 150, "All"] // change per page values here
                ],
                "pageLength": 10, // default record count per page
                "ajax": {
                    "url": "../demo/table_ajax.php", // ajax source
                },
                "order": [
                    [1, "asc"]
                ]// set first column as a default sort by asc
            }
        });

        // handle group actionsubmit button click
        grid.getTableWrapper().on('click', '.table-group-action-submit', function (e) {
            e.preventDefault();
            var action = $(".table-group-action-input", grid.getTableWrapper());
            if (action.val() != "" && grid.getSelectedRowsCount() > 0) {
                grid.setAjaxParam("customActionType", "group_action");
                grid.setAjaxParam("customActionName", action.val());
                grid.setAjaxParam("id", grid.getSelectedRows());
                grid.getDataTable().ajax.reload();
                grid.clearAjaxParams();
            } else if (action.val() == "") {
                App.alert({
                    type: 'danger',
                    icon: 'warning',
                    message: 'Please select an action',
                    container: grid.getTableWrapper(),
                    place: 'prepend'
                });
            } else if (grid.getSelectedRowsCount() === 0) {
                App.alert({
                    type: 'danger',
                    icon: 'warning',
                    message: 'No record selected',
                    container: grid.getTableWrapper(),
                    place: 'prepend'
                });
            }
        });

        //grid.setAjaxParam("customActionType", "group_action");
        //grid.getDataTable().ajax.reload();
        //grid.clearAjaxParams();
    };

    return {
        init: function () {
            handleExercicios();
            initPickers();
            initSelects();
        }

    };

}();