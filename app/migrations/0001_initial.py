# Generated by Django 2.1.1 on 2018-11-26 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('CC_Custo', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('Ativo', models.CharField(max_length=3)),
                ('Descricao', models.CharField(max_length=100)),
                ('Grupo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': '[DBO].[AUX_Grupo_Segmento]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('CPF', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('NOME', models.CharField(max_length=100)),
            ],
            options={
                'db_table': '[DBO].[V_ML_FUNCIONARIO]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('chave_premio', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('dt_inclus', models.DateTimeField()),
                ('ctr_custo', models.CharField(max_length=12)),
                ('tipo', models.PositiveIntegerField()),
                ('competenc', models.CharField(max_length=7)),
                ('observacao', models.CharField(blank=True, max_length=1000, null=True)),
                ('cpf', models.PositiveIntegerField()),
                ('nota_camp', models.CharField(blank=True, max_length=20, null=True)),
                ('vlr_base', models.DecimalField(decimal_places=2, max_digits=7)),
                ('faltas_just', models.CharField(blank=True, max_length=3, null=True)),
                ('faltas_inju', models.CharField(blank=True, max_length=3, null=True)),
                ('vlr_pagar', models.DecimalField(decimal_places=2, max_digits=7)),
                ('estagio', models.PositiveIntegerField()),
                ('solicitante', models.TextField()),
                ('dt_envio_cpa', models.DateTimeField()),
                ('dt_pagamento', models.DateTimeField()),
                ('sit_empre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': '[DBO].[GESTAO_PREMIACAO]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Py_Log_mssql',
            fields=[
                ('pylog_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pylog_etapa_id', models.IntegerField()),
                ('pylog_desc', models.CharField(max_length=200)),
                ('pylog_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': '[DW].[PY_LOG]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sistema_Reload_mssql',
            fields=[
                ('sistema_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sistema_database', models.CharField(max_length=50)),
                ('sistema_server', models.CharField(max_length=15)),
                ('sistema_dw_desc', models.CharField(max_length=50)),
                ('sistema_datetime_start', models.DateTimeField()),
                ('sistema_datetime_finish', models.DateTimeField()),
                ('sistema_erro_flag', models.BooleanField()),
            ],
            options={
                'db_table': '[DW].[SISTEMA_RELOAD]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo_Premio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
            options={
                'db_table': '[DW].[PREMIO_TIPO_ID]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Centralizadora',
            fields=[
                ('id_centralizaora', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('cod_gcpj', models.CharField(max_length=15)),
                ('cod_acao', models.CharField(blank=True, max_length=10, null=True)),
                ('nome_cliente', models.CharField(blank=True, max_length=150, null=True)),
                ('data_email_banco', models.DateTimeField(blank=True, null=True)),
                ('dejur_regional', models.CharField(blank=True, max_length=60, null=True)),
                ('cod_contrato', models.CharField(blank=True, max_length=60, null=True)),
                ('cod_agencia', models.CharField(blank=True, max_length=15, null=True)),
                ('dv_conta', models.IntegerField(blank=True, null=True)),
                ('cod_carteira', models.IntegerField(blank=True, null=True)),
                ('cod_conta', models.CharField(blank=True, max_length=15, null=True)),
                ('filial', models.CharField(blank=True, max_length=60, null=True)),
                ('imagem_notificacao', models.BooleanField()),
                ('data_envio_notificacao', models.DateTimeField(blank=True, null=True)),
                ('data_retorno_notificacao', models.DateTimeField(blank=True, null=True)),
                ('status_notificacao', models.IntegerField(choices=[(0, '-------'), (1, 'Positiva'), (2, 'Negativa'), (3, 'Falecido')], default=0)),
                ('data_envio_protesto', models.DateTimeField(blank=True, null=True)),
                ('data_protesto', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, '-------'), (1, 'Pendencia Banco'), (2, 'Pendencia ML'), (3, 'Concluido'), (4, 'Encerrado')], default=0)),
                ('analise_ajuizamento', models.CharField(choices=[('Ajuizada', [('1.1', 'Inicial Distribuida')]), ('Em Ajuizamento', [('2.1', 'Subfase'), ('2.2', 'Enviado para distribuição'), ('2.3', 'Pgto. Custas'), ('2.4', 'Inicial em fase de Elaboração')]), ('Solicitado Encerramento', [('3.1', 'Subfase'), ('3.2', 'Pagamento'), ('3.3', 'Suplicidade'), ('3.4', 'Falta de Documentação'), ('3.5', 'Não pertence a assessoria'), ('3.6', 'Suspenso ajuizamento'), ('3.7', 'Devolução Amigavel')]), ('Pendente de documentação', [('3.1', 'Subfase'), ('3.2', 'Pagamento'), ('3.3', 'Suplicidade'), ('3.4', 'Falta de Documentação')])], default='1.1', max_length=3)),
                ('viabilidade', models.BooleanField()),
                ('tipo_acao', models.IntegerField(choices=[(0, '-------'), (1, 'Ação de busca e apreensão'), (2, 'Ação de execução'), (3, 'Imovel')], default=0)),
                ('advogado', models.CharField(blank=True, max_length=100, null=True)),
                ('alimentacao_gcpj', models.DateTimeField(blank=True, null=True)),
                ('data_encerramento_gcpj', models.DateTimeField(blank=True, null=True)),
                ('data_contrato_devolvido', models.DateTimeField(blank=True, null=True)),
                ('contrato_hsbc', models.BooleanField()),
                ('data_documento', models.DateTimeField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContratoGcpj',
            fields=[
                ('id_contrato', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('cod_contrato', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetalhamentoInf',
            fields=[
                ('id_detalhamento_inf', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Escopo',
            fields=[
                ('id_escopo', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('responsavel_solicitacao', models.CharField(max_length=100)),
                ('data_solicitacao', models.DateField()),
                ('data_solicitacao_cliente', models.DateField(blank=True, null=True)),
                ('data_conclusao_pretendida', models.DateField()),
                ('favorecidos', models.CharField(max_length=100)),
                ('titulo_solicitacao', models.CharField(max_length=100)),
                ('objetivo', models.CharField(max_length=200)),
                ('fontes', models.CharField(max_length=200)),
                ('outras_inf', models.TextField(max_length=200)),
                ('destinatarios', models.CharField(max_length=100)),
                ('obs_utilizacao', models.CharField(max_length=200)),
                ('obs_resultados', models.CharField(max_length=200)),
                ('obs_impacto_nao_entrega', models.CharField(max_length=200)),
                ('feito_outra_area', models.BooleanField(choices=[(0, 'Não'), (1, 'Sim')], default=0)),
                ('operacao_capacitada', models.BooleanField(choices=[(0, 'Não'), (1, 'Sim')], default=0)),
                ('existe_modelo', models.BooleanField(choices=[(0, 'Não'), (1, 'Sim')], default=0)),
                ('arquivo_modelo', models.FileField(blank=True, null=True, upload_to='arquivos_recebidos')),
                ('e_atividade_plan_mis', models.BooleanField(choices=[(0, 'Não'), (1, 'Sim')], default=0)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Area')),
                ('id_detalhamento_inf', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.DetalhamentoInf')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id_ocorrencia', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('previsao_entrega', models.DateTimeField()),
                ('data_conclusao', models.DateTimeField()),
                ('viabilidade', models.BooleanField()),
                ('obs_viabilidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrigemNumeros',
            fields=[
                ('id_origem_numeros', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrigemRequisito',
            fields=[
                ('id_origem_requisito', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prioridade',
            fields=[
                ('id_prioridade', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrioridadeMl',
            fields=[
                ('id_prioridade_ml', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recorrencia',
            fields=[
                ('id_recorrencia', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsavelPlan',
            fields=[
                ('id_responsavel', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusSolicitacao',
            fields=[
                ('id_status_solicitacao', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTrabalho',
            fields=[
                ('id_tipo_trabalho', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='id_prioridade_ml',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.PrioridadeMl'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='id_responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.ResponsavelPlan'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='id_status_solicitacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.StatusSolicitacao'),
        ),
        migrations.AddField(
            model_name='escopo',
            name='id_origem_numeros',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.OrigemNumeros'),
        ),
        migrations.AddField(
            model_name='escopo',
            name='id_origem_requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.OrigemRequisito'),
        ),
        migrations.AddField(
            model_name='escopo',
            name='id_prioridade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Prioridade'),
        ),
        migrations.AddField(
            model_name='escopo',
            name='id_tipo_trabalho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.TipoTrabalho'),
        ),
    ]