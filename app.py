try:
    import lightrun
    lightrun.enable(company_key='784a727b-f85b-43f2-a6ee-ce5b102bce43')
except ImportError as e:
    print("Error importing Lightrun: ", e)