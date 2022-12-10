package com.aakin.ws;

import com.aakin.ws.model.Product;
import com.aakin.ws.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.List;


@SpringBootApplication
@RequiredArgsConstructor
@Slf4j
public class WsApplication implements CommandLineRunner {
	private final ProductRepository productRepository;
	public static void main(String[] args) {
		SpringApplication.run(WsApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		List<Product> products = productRepository.findByProductNameIsContaining("Billur");
		log.info(products.toString());
	}
}
