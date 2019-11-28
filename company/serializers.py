from .models import Company
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = ['SEQ', 'KEDCD', 'company_name', 'found_date', 'company_size', 'company_type',
            'company_zip', 'company_address', 'business_code1', 'business_code2', 'staff_update_date',
            'staff_number', 'company_main_product', 'company_tel_num', 'closing_2018', 'closing_2017',
            'closing_2016', 'closing_2015', 'closing_2014', 'total_assets_2018', 'total_liabilities_2018',
            'netincome_2018', 'operating_profit_2018', 'total_assets_2017', 'total_liabilities_2017',
            'netincome_2017', 'operating_profit_2017', 'total_assets_2016', 'total_liabilities_2016',
            'netincome_2016', 'operating_profit_2016', 'total_assets_2015', 'total_liabilities_2015',
            'netincome_2015', 'operating_profit_2015', 'total_assets_2014', 'total_liabilities_2014',
            'netincome_2014', 'operating_profit_2014', 'PO_01', 'PO_02', 'PO_03', 'PO_01_num',
            'PO_02_num', 'PO_03_num', 'seller_01', 'seller_02', 'seller_03', 'seller_01_num', 
            'seller_02_num', 'seller_03_num', 'GPS_X', 'GPS_Y']
