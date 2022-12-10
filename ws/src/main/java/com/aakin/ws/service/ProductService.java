package com.aakin.ws.service;


import com.aakin.ws.dto.converter.ProductDto;
import com.aakin.ws.dto.converter.ProductDtoConverter;
import com.aakin.ws.model.Product;
import com.aakin.ws.repository.ProductRepository;
import com.univocity.parsers.common.record.Record;
import com.univocity.parsers.csv.CsvParser;
import com.univocity.parsers.csv.CsvParserSettings;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class ProductService {

    private final ProductDtoConverter productDtoConverter;
    private final ProductRepository productRepository;

    public String createProduct(MultipartFile file) throws IOException {
        List<Product> productList = new ArrayList<>();
        InputStream inputStream = file.getInputStream();
        CsvParserSettings settings = new CsvParserSettings();
        settings.setHeaderExtractionEnabled(true);
        CsvParser parser = new CsvParser(settings);
        List<Record> parseAllRecords = parser.parseAllRecords(inputStream);
        parseAllRecords.forEach(record -> {
            Product product = new Product();
            product.setProductName(record.getString("Product Name"));
            product.setPrice(Double.parseDouble(record.getString("Price")));
            product.setMarketId(Double.parseDouble(record.getString("market_id")));
            productList.add(product);
        });
        productRepository.saveAll(productList);
        return "All data included";
    }

    public List<ProductDto> findAllProducts(){
        List<Product> playerList = productRepository.findAll();
        List<ProductDto> playerDtoList = new ArrayList<>();
        for (Product product : playerList){
            playerDtoList.add(productDtoConverter.convert(product));
        }
        return playerDtoList;
    }

    public List<ProductDto> getProductNameContaining(String index) {
        List<Product> products = productRepository.findByProductNameContaining(index);
        return products.stream().map(productDtoConverter::convert).collect(Collectors.toList());
    }


}