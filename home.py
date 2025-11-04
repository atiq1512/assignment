import streamlit as st

# Add a banner image at the top
banner_image = 'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/3u1i.jpeg' 
st.image(banner_image, use_container_width =True)

#video_url = 'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/Video.mp4' 
# Embed the video as an iframe with autoplay and loop
#st.markdown(f'<iframe width="100%" height="400" src="{video_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', unsafe_allow_html=True)


# Add the main paragraph and explanation
st.write(
    """
    *Program Apprentice 3u1i@FHPK* merupakan sebuah program pengajian mod industri yang dijalankan dengan pelaksanaan struktur kurikulum yang merangkumi tiga tahun pengajian akademik di UMK dan satu tahun latihan industri yang disusun secara sistematik dalam tempoh pengajian di industri terpilih. Program pengajian mod industri yang dijalankan adalah menggunakan kaedah pembelajaran berasaskan kerja (WBL) dengan menggunapakai garis panduan pelaksanaan mod pengajian 2u2i. 
    """
)

banner_image = 'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/3u1i_2.jpeg' 
st.image(banner_image, use_container_width =True)

# Add the main paragraph and explanation
st.write(
    """
    Program Apprentice 3u1i@FHPK telah mula ditawarkan bermula ambilan (kohort) tahun 2018 dan telah memasuki kohort ke-4 pada tahun 2025. Sehingga kini FHPK telah berjaya menghasilkan seramai *202 graduan* daripada program pengajian Mod Industri 3u1i. 

    Sebanyak *14 syarikat* yang terdiri daripada tiga industri utama iaitu *perhotelan, **pelancongan* dan *kesejahteraan* telah terlibat secara langsung dalam penempatan pelajar bagi program ini.
    """
)


st.markdown(
    "[Untuk maklumat lanjut, sila layari Laman Sesawang Fakulti Hospitaliti, Pelancongan dan Kesejahteraan UMK.](https://fhpk.umk.edu.my/program-details.cfm?ref=801&name=---)"
)
